import pytest
from text_processor import count_words, capitalize_words, reverse_text, get_word_count, contains_word, find_longest_word, filter_short_words, save_text_to_file, read_text_from_file, count_sentences, get_average_word_length, remove_punctuation

@pytest.fixture
def sample_text():
    """Provide sample text for tests"""
    # TODO: Return the text "the quick brown fox"
    return "the quick brown fox"

@pytest.fixture
def paragraph():
    """Provide a longer paragraph for testing"""
    # TODO: Return "Python is great. Python is powerful. Python is fun."
    return "Python is great. Python is powerful. Python is fun."

@pytest.fixture
def search_word():
    """Provide a word to search for"""
    # TODO: Return "python"
    return "python"

@pytest.fixture
def word_list():
    """Provide a list of words for testing"""
    # TODO: Return a list: ["cat", "elephant", "dog", "butterfly", "ant"]
    return ["cat", "elephant", "dog", "butterfly", "ant"]

@pytest.fixture
def greeting():
    """Provide a greeting"""
    # TODO: Return "Hello"
    return "Hello"

@pytest.fixture
def name():
    """Provide a name"""
    # TODO: Return "Alice"
    return "Alice"

@pytest.fixture
def full_greeting(greeting, name):
    """Combine greeting and name"""
    # TODO: Return f"{greeting}, {name}!"
    # Example: "Hello, Alice!"
    return f"{greeting}, {name}!"



def test_count_words(sample_text):
    # TODO: Use the sample_text fixture parameter
    # Assert that count_words returns 4
    result = count_words(sample_text)
    assert result == 4

def test_capitalize_words(sample_text):
    # TODO: Use the sample_text fixture parameter
    # Assert that capitalize_words returns "The Quick Brown Fox"
    result = capitalize_words(sample_text)
    assert result == "The Quick Brown Fox"

def test_reverse_text(sample_text):
    # TODO: Use the sample_text fixture parameter
    # Assert that reverse_text returns "xof nworb kciuq eht"
    result = reverse_text(sample_text)
    assert result == "xof nworb kciuq eht"

def test_get_word_count(paragraph):
    # TODO: Test that get_word_count returns {'python': 3, 'is': 3, 'great.': 1, 'powerful.': 1, 'fun.': 1}
    result = get_word_count(paragraph)
    assert result == {'python': 3, 'is': 3, 'great.': 1, 'powerful.': 1, 'fun.': 1}

def test_contains_word(paragraph, search_word):
    # TODO: Test that contains_word(paragraph, search_word) returns True
    result = contains_word(paragraph, search_word)
    assert result == True

def test_find_longest_word(word_list):
    # TODO: Test that find_longest_word returns "butterfly"
    result = find_longest_word(word_list)
    assert result == 'butterfly'

def test_filter_short_words(word_list):
    # TODO: Test that filter_short_words(word_list, 4) returns ["elephant", "butterfly"]
    result = filter_short_words(word_list,4)
    assert result == ["elephant", "butterfly"]

def test_save_text_to_file(tmp_path):
    """Test saving text to a file"""
    # tmp_path is a built-in fixture that provides a temporary directory
    
    # TODO: Create a file path: tmp_path / "test.txt"
    # TODO: Save "Hello, World!" to that file using save_text_to_file
    # TODO: Read the file directly and assert it contains "Hello, World!"
    filepath = tmp_path / "test.txt"
    save_text_to_file("Hello, World!", filepath)
    with open(filepath,'r') as file:
        result = file.read()
    assert result == "Hello, World!"
    

def test_read_text_from_file(tmp_path):
    """Test reading text from a file"""
    # TODO: Create a file path: tmp_path / "input.txt"
    # TODO: Write "Test content" to the file (use file_path.write_text())
    # TODO: Use read_text_from_file to read it
    # TODO: Assert the result is "Test content"
    pathy = tmp_path / "input.txt"
    pathy.write_text("Test content")
    result = pathy.read_text()
    assert result == "Test content"

def test_full_greeting(full_greeting):
    # TODO: Assert full_greeting equals "Hello, Alice!"
    result = full_greeting
    assert result == "Hello, Alice!"

@pytest.fixture
def essay():
    """Provide a multi-sentence essay"""
    # TODO: Return "The cat sat. The dog ran. The bird flew."
    return "The cat sat. The dog ran. The bird flew."

@pytest.fixture
def simple_sentence():
    """Provide a simple sentence with punctuation"""
    # TODO: Return "Hello, world! How are you?"
    return "Hello, world! How are you?"

@pytest.fixture
def cleaned_text():
    """Provide text without punctuation"""
    # TODO: Return "Hello world How are you"
    return "Hello world How are you"

def test_count_sentences(essay):
    # TODO: Test that count_sentences returns 3
    result = count_sentences(essay)
    assert result == 3

def test_get_average_word_length(essay):
    # TODO: Test that average word length is approximately 3.0
    # Hint: Words are ["The", "cat", "sat", "The", "dog", "ran", "The", "bird", "flew"]
    # Average = (3+3+3+3+3+3+3+4+4) / 9 = 29/9 ≈ 3.22
    result = get_average_word_length(essay)
    assert result == 29/9

def test_remove_punctuation(simple_sentence, cleaned_text):
    # TODO: Test that remove_punctuation(simple_sentence) returns cleaned_text
    result = remove_punctuation(simple_sentence)
    assert result == cleaned_text