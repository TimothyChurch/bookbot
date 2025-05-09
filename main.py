from stats import get_word_count, charater_count
import sys

if len(sys.argv) < 2:
    print('Usage: python3 main.py <path_to_book>')
    sys.exit(1)
else:
    path = sys.argv[1]
    def get_book_text(filepath):
        with open(filepath) as filepath:
            contents = filepath.read()
            return contents

    contents = get_book_text(path)

    count = get_word_count(contents)
    character_list = charater_count(contents)

    print('============ BOOKBOT ============')
    print('Analyzing book found at books/frankenstein.txt...')
    print('----------- Word Count ----------')
    print(f'Found {count} total words')
    print('----------- Character Count --------')
    for char in character_list:
        print(f'{char["char"]}: {char["num"]}')
    print('============= END ===============')
