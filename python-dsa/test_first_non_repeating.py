# Testing first_non_repeating.py
import pytest
from first_non_repeating import first_non_repeating

def test_non_repeating_aaa():
    assert first_non_repeating("aaa") == None

def test_non_repeating_begining():
    assert first_non_repeating("hello") == "h"

def test_non_repeating_end():
    assert first_non_repeating("aaabbbcccd") == "d"

def test_non_repeating_middle():
    assert first_non_repeating("aaabccc") == "b"

def test_non_repeating_mixed():
    assert first_non_repeating("aaa222bb3cd3") == "c"

def test_non_repeating_non_string():
    with pytest.raises(TypeError):
        first_non_repeating(123)