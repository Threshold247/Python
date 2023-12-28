import time

current_time = time.time()


def speed_calc_decorator(function):

    def wrapper():
        start = time.time()
        function()
        end = time.time()
        difference = end-start
        print(f"{function.__name__} run speed is:{difference} seconds")
    return wrapper


@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        i * i


@speed_calc_decorator
def slow_function():
    for i in range(100000000):
        i * i


fast_function()
slow_function()
