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
    count = num
    if num == 0:
        return 1
    elif num == 1:
        return count
    else:
        count += count * factorial_summer(num - 1)


    



