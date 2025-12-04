# Problem:
# Write a function that reverses a string without using slicing or reversed().

# Deliverables:
# ✔ clean function
# ✔ docstring
# ✔ 1–2 pytest tests

def reverse_string (word):
    """
    Reverses the content of a string using while loop

    Args:
        word (str): word or phrase to reverse
        
    Returns:
        str: a string with characters in reverse order
        
    Raises:
        TypeError 
    """
    if not isinstance(word, str):
        raise TypeError ("word must be a string")

    i = len(word)
    reversed_word = ""
    while 0 < i:
        reversed_word = reversed_word + word[i-1]
        i = i-1
    return reversed_word

if __name__ == "__main__":
    string = "hello world!"
    print (string)
    print (f"Reversed: {reverse_string(string)}")