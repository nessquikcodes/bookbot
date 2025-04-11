def get_num_of_words(text: str)->int:
    """
    Returns the number of words in a string.
    """
    return len(text.split())

def get_char_count(text: str)->dict:
    """
    Returns the number of occurrances for each character in a string.
    """
    text = text.lower()
    char_count = {' ': 0}
    for char in text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count