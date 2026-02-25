from modules.helpers import adder

print(adder(1,2))

def divide(a,b):
    return a / b

try:
    result = divide(10,2)
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
else:
    print("Result:", result)

import pytest

@pytest.fixture
def test_file(tmp_path): 
    """Create a temporary test file"""
    file_path = tmp_path / "test.txt"
    file_path.write_text("Hello, World!")
    return file_path

def test_file_content(test_file):
    content = test_file.read_text()
    assert content == "Hello, World!"

def test_file_exists(test_file):
    assert test_file.exists()

# project/
# ├── conftest.py          # Shared fixtures here
# ├── test_math.py
# └── test_strings.py

# conftest.py
import pytest

@pytest.fixture
def sample_list():
    """Available to all test files"""
    return [1, 2, 3, 4, 5]

##########################################

#test_math.py
def test_sum(sample_list):  # don't need import
    assert sum(sample_list) == 18

##########################################

#test_strings.py
def test_length(sample_list):  # Same fixture available here
    assert len(sample_list) == 5


with open('names.txt', 'r') as f:
    # enumerate(file, start=1) gives you (1, line), (2, line), etc.
    for line_num, line in enumerate(f, start=1):
        print(f"Line {line_num}: {line.strip()}")