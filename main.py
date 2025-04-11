"""
Book Bot
This script reads a text file containing a book and provides functions to analyze the text.
"""
from stats import get_num_of_words, get_char_count

def get_book_text(path_to_file: str)-> str:
    """
    Reads a text file and returns its contents as a string.
    """
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def main():
    print("Welcome to the Book Bot!\n")
    # Get the path to the book file
    path_to_file = "./books/frankenstein.txt"
    
    # Get the text of the book
    book_text = get_book_text(path_to_file)
    num_words = get_num_of_words(book_text)
    
    print(f"{num_words} words found in the document")
    
    # Get the character count
    char_count = get_char_count(book_text)
    print("Character count:")
    print(char_count)
    
if __name__ == "__main__":
    main()