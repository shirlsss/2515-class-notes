def calculate(*args, **kwargs):
    total = 0
    for num in args:
        total += int(num)
    multiplier = kwargs.get("multiplier",1)
    bonus = kwargs.get("bonus",0)
    total = total * multiplier + bonus
    return total

# Test cases:
print(calculate(1, 2, 3))                    # Should return 6
print(calculate(1, 2, 3, multiplier=2))      # Should return 12
print(calculate(1, 2, 3, bonus=10))          # Should return 16
print(calculate(1, 2, 3, multiplier=2, bonus=5))  # Should return 17