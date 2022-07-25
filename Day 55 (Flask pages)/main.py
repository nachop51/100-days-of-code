# Create the logging_decorator() function 👇

def logging_decorator(function):
    def wrapper(*args, **kwargs):
        str = ""
        if args:
            for arg in args:
                if arg != args[0]:
                    str += ', '
                str += f"{arg}"
        print(f"You called {function.__name__}({str})")
        print(f"It returned: {function(*args, **kwargs)}")
    return wrapper
# Use the decorator 👇


@logging_decorator
def a_function(a, b, c):
    return a + b + c


a_function(1, 2, 3)
