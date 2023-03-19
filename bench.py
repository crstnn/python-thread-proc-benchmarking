from time import perf_counter
from thread import do_thread_count
from proc import do_proc_count
from utils import do_serial_count

NUMBER_OF_THREAD_PROC = 10
MAX_COUNT = 100000


def do_time(func: callable):
    start_time = perf_counter()
    result = func(NUMBER_OF_THREAD_PROC, MAX_COUNT)
    end_time = perf_counter()
    return result, end_time - start_time


result, time = do_time(do_serial_count)
print(f'Serial result: {result}, '
      f'Time taken: {time:.4f} seconds')

result, time = do_time(do_thread_count)
print(f'Threading result: {result}, '
      f'Time taken: {time:.4f} seconds')

result, time = do_time(do_proc_count)
print(f'Multiprocessing result: {result}, '
      f'Time taken: {time:.4f} seconds')
