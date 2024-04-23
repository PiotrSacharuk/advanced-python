import functools


def log_function_data(func):
    """
    Decorator to log function call details: function name, arguments, and return value.
    """
    @functools.wraps(func)  # Preserves function metadata
    def wrapper(*args, **kwargs):
        # Log function arguments and their values
        args_repr = [repr(a) for a in args]                      # Argument values
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]  # Keyword argument values
        signature = ", ".join(args_repr + kwargs_repr)           # Stitch together the signature string
        print(f"Calling {func.__name__}({signature})")
        # Call the function and get the return value
        value = func(*args, **kwargs)
        print(f"{func.__name__!r} returned {value!r}")           # Log the return value
        return value
    return wrapper


# Example use of the decorator
@log_function_data
def add(a, b):
    """Add two numbers together."""
    return a + b


# Calling the decorated function
result = add(5, 3)
