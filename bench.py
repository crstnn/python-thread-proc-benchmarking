from time import perf_counter
from thread import do_thread_count_1
from proc import do_proc_count
from utils import do_serial_count

NUMBER_OF_THREAD_PROC = 8
MAX_COUNT = 1000000 // NUMBER_OF_THREAD_PROC


def do_time(func: callable):
    start_time = perf_counter()
    result = func(NUMBER_OF_THREAD_PROC, MAX_COUNT)
    end_time = perf_counter()
    return result, end_time - start_time


result, time = do_time(do_serial_count)
print(f'Serial result: {result}, '
      f'Time taken: {time:.4f} seconds')

result, time = do_time(do_thread_count_1)
print(f'Threading (using `multiprocessing` shared var) result: {result}, '
      f'Time taken: {time:.4f} seconds')

result, time = do_time(do_proc_count)
print(f'Multiprocessing result: {result}, '
      f'Time taken: {time:.4f} seconds')
