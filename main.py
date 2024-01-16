def main():
    file = "books/frankenstein.txt"
    text = get_text(file)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    chars_sorted_list = chars_dict_sort_alpha(chars_dict)

    print(f"--- Begin report of {file} ---")
    print(f"{num_words} words were found in the document.\n")
    
    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times.")
    
    print(f"--- End report ---")
                    

def get_text(file):
    with open(file) as f:
        # returns the contents of the text file
        return f.read()

# counts the number of words in a text
def get_num_words(text):
    words = text.split()
    return len(words)

def sort_on(d):
    return d["num"]

def chars_dict_sort_alpha(chars_dict):
    chars_list = []
    for ch in chars_dict:
        chars_list.append({"char": ch, "num": chars_dict[ch]})
    chars_list.sort(reverse=True, key=sort_on)
    return chars_list

# counts the number of times each character appears in the text
def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

main()