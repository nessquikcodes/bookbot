def main():
    file = "books/frankenstein.txt"
    text = get_text(file)
    num_words = get_num_words(text)
    print(f"{num_words} words were found in the document.")
    num_chars = get_num_letters(text)
    print(f"{num_chars}")

def get_text(file):
    with open(file) as f:
        # returns the contents of the text file
        return f.read()

# counts the number of words in a text
def get_num_words(text):
    words = text.split()
    return len(words)

# counts the number of times each character appears in the text
def get_num_letters(text):
    letters = {}
    count = 0

    for i in range(len(text)):
        if text[i] not in letters:
            count = 1
        else:
            count =+ 1
        letters = dict({text[i]: count})
    return text[i]

main()