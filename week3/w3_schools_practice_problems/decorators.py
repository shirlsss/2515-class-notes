"""
https://www.w3resource.com/python-exercises/decorator/index.php

1. Create a Decorator to Log Function Arguments and Return Value

Write a Python program to create a decorator that logs the arguments and return value of a function.

"""

from functools import wraps

def log_decorator(func):
    @wraps(func)
    def log_wrapper(*args,**kwargs):
        result = func(*args, **kwargs)
        print(f"Logging arguments: {args, kwargs}")
        return result 
    return log_wrapper

@log_decorator
def adder(a, b):
    return a + b

adder(3,4)
