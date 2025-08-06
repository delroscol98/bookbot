def get_num_words(text_from_book):
    words = text_from_book.split()
    return len(words)

def get_num_chars(text_from_book):
    char_count_dict = {}
    for char in text_from_book:
        if char.lower() not in char_count_dict:
            char_count_dict[char.lower()] = 1
        else:
            char_count_dict[char.lower()] += 1

    return char_count_dict

def sort_on(items):
    return items["num"]

def get_sorted_char_dict(char_count_dict):
    chars = []

    for char, num in char_count_dict.items():
        chars.append({ "char": char, "num": num})

    chars.sort(reverse=True, key=sort_on)

    return chars
