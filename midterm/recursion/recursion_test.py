from recursion_practice import sum_of_list, factorial_summer

def test_sum_normalcase():
    nums = [1, 2, 3]
    result = sum_of_list(nums)
    assert result == 6

def test_sum_mix_nums():
    nums = [1, -2, -5, [2, 1]]
    result = sum_of_list(nums)
    assert result == -3

def test_sum_add_zeros():
    nums = [0, 0, 0, [1, 2, 3], 5]
    result = sum_of_list(nums)
    assert result == 11

def test_sum_add_all_lists():
    nums = [[1,1,1,1],[2],[3,4]]
    result = sum_of_list(nums)
    assert result == 13

def test_factorial_normal():
    num = 4
    result = factorial_summer(4)
    assert result == 24

def test_factorial_zero():
    num = 0
    result = factorial_summer(0)
    assert result == 1