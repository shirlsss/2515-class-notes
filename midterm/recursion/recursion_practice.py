# 1. Sum of List Using Recursion
# Write a Python program to calculate the sum of a list of numbers using recursion.

nums1 = [1, 2, 3, [4, 2], [1], 2]

def sum_of_list(nums: list) -> int:
    sum = 0
    for num in nums:
        if isinstance(num,int):
            sum += num
        elif isinstance(num,list):
            sum += sum_of_list(num)
    return sum


# 4. Factorial Using Recursion
# Write a Python program to get the factorial of a non-negative integer using recursion.
# Example: !4 = 4 x 3 x 2 x 1 = 24

def factorial_summer(num: int) -> int:
    if num <= 1:
        return 1
    return num * factorial_summer(num - 1)


# Create a function that accepts any number of numbers and any keyword arguments, then:

# Sum all the numbers from *args
# Multiply the sum by a multiplier from **kwargs (default to 1)
# Add a bonus from **kwargs (default to 0)

def calculate(*args, **kwargs):
    nums = sum(args)
    multiplier = kwargs.get("multiplier",1)
    bonus = kwargs.get("bonus",0)
    return nums * multiplier + bonus

# Test cases:
print(calculate(1, 2, 3))                    # Should return 6
print(calculate(1, 2, 3, multiplier=2))      # Should return 12
print(calculate(1, 2, 3, bonus=10))          # Should return 16
print(calculate(1, 2, 3, multiplier=2, bonus=5))  # Should return 17


# Accept any number of keyword arguments using **kwargs
# Required fields: name and email - raise ValueError if missing
# Optional fields with defaults:
# role (default: "user")
# active (default: True)
# Store any additional fields passed in **kwargs
# Return a dictionary with all the profile information

def create_user_profile(**kwargs):
    user_profile = {}
    if "name" not in kwargs:
        raise ValueError("Error: Missing name!")
    elif "email" not in kwargs:
        raise ValueError("Error: Missing email!")
    else:
        user_profile["name"] = kwargs.get("name")
        user_profile["email"] = kwargs.get("email")
        user_profile["role"] = kwargs.get("role","user")
        user_profile["active"] = kwargs.get("active", True)
        for k, v in kwargs.items():
            if k != "name" and k != "email":
                user_profile[k] = v
    return user_profile

# Test cases:
print(create_user_profile(name="Alice", email="alice@example.com"))
# Should return: {'name': 'Alice', 'email': 'alice@example.com', 'role': 'user', 'active': True}

print(create_user_profile(name="Bob", email="bob@example.com", role="admin"))
# Should return: {'name': 'Bob', 'email': 'bob@example.com', 'role': 'admin', 'active': True}

print(create_user_profile(name="Charlie", email="charlie@example.com", age=30, city="Vancouver"))
# Should return: {'name': 'Charlie', 'email': 'charlie@example.com', 'role': 'user', 'active': True, 'age': 30, 'city': 'Vancouver'}

# This should raise ValueError:
# create_user_profile(name="Dave")  # Missing email
