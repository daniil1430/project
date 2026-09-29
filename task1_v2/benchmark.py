import random
import time
import statistics
from main import max_subarray_v1

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

def main():
    size_v1 = [64, 128, 256]

    print("Алгоритм 1")
    for n in size_v1:
        arr = random_arr(n)
        t = benchmark(max_subarray_v1, arr)
        size_bytes = n * 8
        print(n, size_bytes,t)

if __name__ == "__main__":
    main()