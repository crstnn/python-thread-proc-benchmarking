import multiprocessing
from utils import increment_counter_for_parallel


def do_proc_count(n, max_count):
    counter = multiprocessing.Value('i', 0)

    threads = []
    for i in range(n):
        t = multiprocessing.Process(target=increment_counter_for_parallel, args=(counter, max_count))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    return counter.value
