import timeit


# Python caches small integers (typically between -5 and 256) to optimize memory usage and performance.
# This means that these integers are reused, and comparisons between them are faster.
# We can measure the performance impact of interning by observing the time taken for operations
# involving integers inside and outside this range.


def measure_interning_performance(start: int, repeats: int) -> int:
    total = 0
    for _ in range(repeats):
        for i in range(start, start + 200):
            total += i

    return total


elapsed1 = timeit.timeit("measure_interning_performance(0, 1000000)", globals=globals(), number=1)
elapsed2 = timeit.timeit("measure_interning_performance(50, 1000000)", globals=globals(), number=1)
elapsed3 = timeit.timeit("measure_interning_performance(1000, 1000000)", globals=globals(), number=1)


print(f"Elapsed time for integers starting at 0: {elapsed1:.4f} seconds")
print(f"Elapsed time for integers starting at 50: {elapsed2:.4f} seconds")
print(f"Elapsed time for integers starting at 1000: {elapsed3:.4f} seconds")
