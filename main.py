"""
Book Bot
This script reads a text file containing a book and provides functions to analyze the text.
"""
from stats import get_num_words, get_char_count, sort_on

def get_book_text(path_to_file: str)-> str:
    """
    Reads a text file and returns its contents as a string.
    """
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def main():
    print("============ BOOKBOT ============")
    # Get the path to the book file
    path_to_file = "./books/frankenstein.txt"
    print(f"Analyzing book found at {path_to_file}...")
    
    # Get the text of the book
    book_text = get_book_text(path_to_file)
    
    print("----------- Word Count ----------")
    # Get the number of words
    num_words = get_num_words(book_text)
    print(f"Found {num_words} total words")
    
    print("--------- Character Count -------")
    # Get the character count
    char_count = get_char_count(book_text)
    #print(char_count)        
    sorted_char_count = []
    for char, count in char_count.items():
        if char.isalpha():
            sorted_char_count.append({'char': char, 'count': count})
    sorted_char_count.sort(reverse=True, key = sort_on)
    
    for sorted_char in sorted_char_count:
        print(f'{sorted_char['char']}: {sorted_char['count']}')
    
    print("============= END ===============")
    
if __name__ == "__main__":
    main()