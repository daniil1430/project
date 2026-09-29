import random
import time
import statistics

def benchmark(func, arr):
    for i in range(3):
        func(arr)

    times = []
    for i in range(7):
        start = time.perf_counter_ns()
        func(arr)
        end = time.perf_counter_ns()
        times.append(end - start)
    return statistics.median(times)


def random_arr(n):
    return [random.randint(-1000, 1000) for i in range(n)]