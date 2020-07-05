import time


def get_sequence(n):
    if n <= 0:
        return 1
    else:
        v = 0
        for i in range(n):
            v += 1 + (get_sequence(i - 1) + get_sequence(i)) / 2
        return v


print(get_sequence(3))


def wrapper_time(a_function):
    def a_wrapped_function(*args, **kwargs):
        time_start = time.time()
        v = a_function(*args, **kwargs)
        time_stop = time.time()
        print("Function {} end in time: {}".format(a_wrapped_function.__name__, (time_stop - time_start)))
        return v
    return a_wrapped_function


wrapper_get_sequence = wrapper_time(get_sequence)
print(wrapper_get_sequence(18))
print(wrapper_get_sequence(19))
print(wrapper_get_sequence(20))

'''
# modyfikacja z logowaniem
import time
import functools


def wrapper_time(a_function):
    def a_wrapped_function(*args, **kwargs):
        time_start = time.time()
        v = a_function(*args, **kwargs)
        time_stop = time.time()
        print("Function {} end in time: {}".format(a_wrapped_function.__name__, (time_stop - time_start)))
        return v
    return a_wrapped_function


@wrapper_time
def get_sequence(n):
    if n <= 0:
        return 1
    else:
        v = 0
        for i in range(n):
            v += 1 + (get_sequence(i - 1) + get_sequence(i)) / 2
        return v


print(get_sequence(10))
'''
