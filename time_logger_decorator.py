
import time
import functools

def time_logger(func):
    """A decorator that measures and logs the execution time of a function."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        time_taken = end_time - start_time
        print(f"Function '{func.__name__}' executed in {time_taken:.4f} seconds.")
        return result
    return wrapper

