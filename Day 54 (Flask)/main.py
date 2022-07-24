import time
current_time = time.time()
# print(current_time)


def speed_calc_decorator(function):
    def hello():
        before = time.time()
        function()
        print(f"{function.__name__} run speed: {time.time() - before}s")
    return hello


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
