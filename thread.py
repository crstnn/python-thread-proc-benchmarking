import threading
import multiprocessing
from utils import increment_counter_for_parallel
multiprocessing.freeze_support()


def do_thread_count(n, max_count):
    counter = multiprocessing.Value('i', 0)

    threads = []
    for i in range(n):
        t = threading.Thread(target=increment_counter_for_parallel, args=(counter, max_count))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    return counter.value
