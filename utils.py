def increment_counter_for_parallel(counter, max_count):
    for _ in range(max_count):
        with counter.get_lock():
            counter.value += 1


def increment_counter_for_serial(counter, max_count):
    for _ in range(max_count):
        counter += 1
    return counter


def do_serial_count(n, max_count):
    counter = 0
    counter = increment_counter_for_serial(counter, n * max_count)
    return counter
