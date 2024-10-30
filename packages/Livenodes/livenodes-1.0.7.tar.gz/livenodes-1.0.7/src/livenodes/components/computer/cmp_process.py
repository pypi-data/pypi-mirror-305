
import logging
from logging.handlers import QueueHandler
import threading as th
import multiprocessing as mp
from itertools import groupby
from livenodes.components.utils.log import drain_log_queue
from livenodes.components.node_logger import Logger

from .cmp_thread import Processor_threads


class Processor_process(Logger):
    def __init__(self, nodes, location, bridges, stop_timeout_threads=0.1, close_timeout_threads=0.1) -> None:
        super().__init__()
        # -- both processes
        # indicates that the subprocess is ready
        self.ready_event = mp.Event() 
        # indicates that the readied nodes should start sending data
        self.start_lock = mp.Lock() 
        # indicates that the started nodes should stop sending data
        self.stop_lock = mp.Lock() 
        # indicates that the thread should be closed without waiting on the nodes to finish
        self.close_lock = mp.Lock() 
        # used for logging identification
        self.location = location
        # tell log drainer thread that it should return 
        self.worker_log_handler_termi_sig = th.Event()

        # -- main process
        self.nodes = nodes
        self.bridges = bridges
        self.subprocess = None
        self.start_lock.acquire()
        self.stop_lock.acquire()
        self.close_lock.acquire()

        # -- worker process
        self.stop_timeout_threads = stop_timeout_threads
        self.close_timeout_threads = close_timeout_threads

        self.info(f'Creating Process Computer with {len(self.nodes)} nodes.')


    def __str__(self) -> str:
        return f"CMP-PR:{self.location}"

    # parent process
    def setup(self):
        self.info('Readying')

        parent_log_queue = mp.Queue()
        logger_name = 'livenodes'
        
        self.worker_log_handler = th.Thread(target=drain_log_queue, args=(parent_log_queue, logger_name, self.worker_log_handler_termi_sig))
        self.worker_log_handler.deamon = True
        self.worker_log_handler.name = f"LogDrain-{self.worker_log_handler.name.split('-')[-1]}"
        self.worker_log_handler.start()

        self.subprocess = mp.Process(
                        target=self.start_subprocess,
                        args=(self.bridges, parent_log_queue, logger_name,), name=str(self))
        self.subprocess.start()
        
        self.info('Waiting for worker to be ready')
        self.ready_event.wait(timeout=10)
        self.info('Worker ready, resuming')

    # parent process
    def start(self):
        self.info('Starting')
        self.start_lock.release()

    # TODO: this will not work
    # as: the start() of the thread processor used inside of this processors supbrocess are non-blockign
    # therefore: we are waiting on the stop-lock which will be released once someone calls stop -> thus joining the subprocess will never return!
    # in the join case we would want to be able to join each thread cmp instead of waiting on stop or close...
    # FIXED: inside of the subprocess we are short_ciruiting the stop and close locks if the threads have returned by themselves, thus the join returns once close is called or the sub-threads return
    # parent process
    def join(self, timeout=None):
        """ used if the processing is nown to end"""
        self.info('Joining')
        self.subprocess.join(timeout)

    # parent process
    def stop(self, timeout=0.3):
        """ used if the processing is nown to be endless"""

        self.info('Stopping')
        self.stop_lock.release()
        self.subprocess.join(timeout)
        self.info('Returning; Process finished: ', not self.subprocess.is_alive())

    # parent process
    def close(self, timeout=0.5):
        self.info('Closing')
        self.close_lock.release()
        self.subprocess.join(timeout)
        if self.subprocess.is_alive():
            self.subprocess.terminate()
            self.info('Timout reached: killed process')
        # self.subprocess = None
        self.info('Closing Log Drain')
        self.worker_log_handler_termi_sig.set()

    # parent thread
    def is_finished(self):
        return self.subprocess is not None and not self.subprocess.is_alive()
        
    # worker process
    def check_threads_finished(self, computers):
        return all([cmp.is_finished() for cmp in computers])

    # worker process
    def start_subprocess(self, bridges, subprocess_log_queue, logger_name):
        logger = logging.getLogger(logger_name)
        logger.addHandler(QueueHandler(subprocess_log_queue))
        logger.propagate = False # this fixes duplicate log entries. I'm not fully sure why, but i'm assuming that in case of forking the logger propagates to the parent logger and thus the log is duplicated
        # however, we should double check once we moved to spawn everywhere, bc this whole drain queue migh not be necessary after all...

        self.info('Starting Process')

        computers = []
        # TODO: it's a little weird, that bridges are specifically passed, but nodes are not, we should investigate that
        # ie, probably this is fine, as we specifcially need the bridge endpoints, but the nodes may just be pickled, but looking into this never hurts....
        bridge_lookup = {str(node): bridge for node, bridge in zip(self.nodes, bridges)}

        locations = groupby(sorted(self.nodes, key=lambda n: n.compute_on), key=lambda n: n.compute_on)
        for loc, loc_nodes in locations:
            loc_nodes = list(loc_nodes)
            self.info(f'Resolving computer group. Location: {loc}; Nodes: {len(loc_nodes)}')
            node_specific_bridges = [bridge_lookup[str(n)] for n in loc_nodes]
            cmp = Processor_threads(nodes=loc_nodes, location=loc, bridges=node_specific_bridges)
            computers.append(cmp)
        
        self.info('Created computers:', list(map(str, computers)))
        self.info('Setting up computers')
        for cmp in computers:
            cmp.setup()

        self.info('All Computers ready')
        self.ready_event.set()

        
        self.start_lock.acquire()
        self.info('Starting Computers')
        for cmp in computers:
            # this is non-blocking -> this process will lock until the stop_lock can be aquired
            # inside of this process all sub-threads will run until stop is called
            cmp.start()


        all_computers_finished = False
        while not self.stop_lock.acquire(timeout=0.1) and not all_computers_finished:
            all_computers_finished = all([cmp.is_finished() for cmp in computers])
        
        if all_computers_finished:
            self.info('All Computers have finished, returning')
        else:
            self.info('Stopping Computers')
            for cmp in computers:
                # the cmps are all returning after the timeout, as they all are Processor_Threads
                # -> therefore, this cannot block indefinetly and we can soon wait on the close_lock
                cmp.stop(timeout=self.stop_timeout_threads)

            # if not all_computers_finished:
            self.close_lock.acquire()
            self.info('Closing Computers')
            for cmp in computers:
                cmp.close(timeout=self.close_timeout_threads)

        self.info('Finished Process and returning')
