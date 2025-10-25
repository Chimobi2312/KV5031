
import time
from time_logger_decorator import time_logger

@time_logger
def slow_function(seconds):
    time.sleep(seconds)
    return "Function complete!"

@time_logger
def add(a, b):
    return a + b

# Calling the decorated functions
result1 = slow_function(2)
print(result1)

result2 = add(5, 7)
print(result2)

