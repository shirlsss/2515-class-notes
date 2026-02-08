from calculator import add
from calculator import subtract
from calculator import multiply
from calculator import is_even


def test_add():
    """Test that add function works correctly"""
    result = add(2,3)
    assert result == 5

def test_add_positive_numbers():
    """Test adding two positive numbers"""
    result = add(2,3)
    assert result == 5

def test_add_negative_numbers():
    """Test adding two negative numbers"""
    result = add(-2,-2)
    assert result == -4

def test_add_zero():
    """Test adding zero to a number"""
    result = add(0,2)
    assert result == 2

def test_subtract():
    result = subtract(5,3)
    assert result == 2

def test_subtract_negative_result():
    """Test subtraction that results in negative"""
    # TODO: Write test for subtract(3, 5) -> -2
    result = subtract(3,5)
    assert result == -2

def test_subtract_zero():
    """Test subtracting zero"""
    # TODO: Write test for subtract(5, 0) -> 5
    result = subtract(5,0)
    assert result == 5

def test_multiply_positive_numbers():
    result = multiply(2,2)
    assert result == 4

def test_multiply_positive_negative():
    result = multiply(2,-2)
    assert result == -4

def test_multiply_zero():
    result = multiply(2,0)
    assert result == 0

def test_multiply_one():
    result = multiply(2,1)
    assert result == 2

def test_is_even_even_numbs():
    result = is_even(2)
    assert result == True

def test_is_even_odd():
    result = is_even(3)
    assert result == False

def test_is_even_zero():
    result = is_even(0)
    assert result == True

def test_is_even_negative():
    result = is_even(-2)
    result2 = is_even(-3)
    assert result == True
    assert result2 == False

