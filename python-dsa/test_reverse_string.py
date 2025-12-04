# Test suite for the reverse_string.py function
import pytest
from reverse_string import reverse_string

def test_reverse_string_lowercase():
    assert reverse_string("hello") == "olleh"

def test_reverse_string_empty():
    assert reverse_string("") == ""

def test_reverse_string_mix():
    assert reverse_string("hT2# @3d. ") == " .d3@ #2Th"

def test_reverse_string_not_a_string():
    i = 1230
    with pytest.raises(TypeError) as exc_info:
        reverse_string(i)

    assert str(exc_info.value) == "word must be a string"