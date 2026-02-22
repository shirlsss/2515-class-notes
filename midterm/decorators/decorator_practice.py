#1. Create a Decorator to Log Function Arguments and Return Value
# Write a Python program to create a decorator that logs the arguments and return value of a function.

def log_args(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"Logging the args...\nargs:{args}\nkwargs:{kwargs}")
        print(f"Return value of: {result}")
        return result
    return wrapper

@log_args
def print_names(*args, **kwargs):
    for k,v in kwargs.items():
        print(f"Key:{k}, Value:{v}")

print_names(name="Shirley")

# Create a function that accepts any number of numbers and any keyword arguments, then:

# Sum all the numbers from *args
# Multiply the sum by a multiplier from **kwargs (default to 1)
# Add a bonus from **kwargs (default to 0)

def calculate(*args, **kwargs):
    sums = sum(*args)
    pass

# # Test cases:
# print(calculate(1, 2, 3))                    # Should return 6
# print(calculate(1, 2, 3, multiplier=2))      # Should return 12
# print(calculate(1, 2, 3, bonus=10))          # Should return 16
# print(calculate(1, 2, 3, multiplier=2, bonus=5))  # Should return 17