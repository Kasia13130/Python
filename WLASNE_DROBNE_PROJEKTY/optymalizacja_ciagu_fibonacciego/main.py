'''
import time


def fibonacci(n):
    if n == 0:
        result = 0
    elif n == 1:
        result = 1
    elif n > 1:
        result = fib(n - 1) + fib(n - 2)

    return result


start = time.time()
for n in range(1, 37):
    stop = time.time()
    print("{} = {} at time: {:.4}".format(n, fib(n), stop - start))
print("End of calculation: {:.5}".format(stop - start))
'''


# -----
# po optymalizacji funkcji
import time
import functools


@functools.lru_cache(100)
def fibonacci(n):
    if n == 0:
        result = 0
    elif n == 1:
        result = 1
    elif n > 1:
        result = fib(n - 1) + fib(n - 2)

    return result


start = time.time()
for i in range(1, 37):
    stop = time.time()
    print("{} = {} at time: {:.4}".format(i, fib(i), stop - start))
print("End of calculation: {:.5}".format(stop - start))

print(fib.cache_info())

