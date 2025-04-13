def get_num_words(text: str)->int:
    """
    Returns the number of words in a string.
    """
    return len(text.split())    

def get_char_count(text: str):
    """
    Returns the number of occurrances for each character in a string.
    """
    text = text.lower()
    char_count = {}
    count = 1
    for char in text:   
        if char in char_count:
            counter = char_count[char] + 1
            char_count[char] = counter
        else:
            char_count[char] = count
                    
    return  char_count

def sort_on(dict):
    """
    A function that takes a dictionary and returns the value of the "count" key
    """
    return dict("count")