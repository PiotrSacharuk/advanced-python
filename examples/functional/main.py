import time
import functools

def exp(e):
    def inner(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            value = func(*args, **kwargs)
            new_value = []
            for x in value:
                new_value.append(x**e)
            return new_value
        return wrapper
    return inner


@exp(4)
def get_values(x):
    return list(range(x))


print(get_values(5))