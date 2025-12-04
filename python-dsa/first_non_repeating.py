# Problem:
# Return the first non-repeating character in a string.
# If none exists, return None.

# Deliverables:
# ✔ clean function
# ✔ docstring
# ✔ 1–2 pytest tests

def first_non_repeating(string):
    """
    Finds and returns the first non-repeating character in a string.
    
    Args:
        string (str): string to look for repeating character

    Returns:
        str or None: the first non-repeating character, or None if none exists.

    Raises:
        TypeError: when string is not a str
    """
    if not isinstance(string, str):
        raise TypeError ('string must be a str')

    i, j = 0, 0 # initializing double loop
    char_count = 0
    evaluated_character = ""
    while i < len(string):
        evaluated_character = string[i] 
        j = 0 # resetting our inner loop counter
        while j < len(string):
            if evaluated_character == string[j]:
                char_count += 1
            j += 1
        if char_count == 1:
            return evaluated_character
        char_count = 0 # resetting our counter for next iteration
        i += 1
    return None