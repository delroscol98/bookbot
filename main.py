import sys

from stats import get_num_words
from stats import get_num_chars
from stats import get_sorted_char_dict

def get_book_text(path_to_file):
    file_contents = None
    with open(path_to_file) as f:
        file_contents = f.read()

    return file_contents

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path_to_book = sys.argv[1]
    book_text = get_book_text(path_to_book)
    char_count_dict = get_num_chars(book_text)
    sorted_char_dict = get_sorted_char_dict(char_count_dict)

    print('===============BOOKBOT===============')
    print('Analysing book found at ' + path_to_book + '...'
    print('----- Word Count --------------------')
    print(f'Found {get_num_words(book_text)} total words')
    print('----- Character Count ---------------')
    for i in range(len(sorted_char_dict)):
        char = sorted_char_dict[i]['char']
        num = sorted_char_dict[i]['num']

        if char.isalpha() == True:
            print(f"{char}: {num}")
            


main()
