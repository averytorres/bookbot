import sys
from stats import get_num_words
from stats import char_count
from stats import dict_report

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def main():
    if len(sys.argv) != 2:
        print(f"Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        file_loc = sys.argv[1]

        book_text = get_book_text(file_loc)
        num_words = get_num_words(str(book_text))
        raw_dict = char_count(book_text)
        sorted_dict = dict_report(raw_dict)

        print(f"============ BOOKBOT ============")
        print(f"Analyzing book found at {file_loc}...")
        print(f"----------- Word Count ----------")
        print(f"Found {num_words} total words")
        print(f"--------- Character Count -------")

        for letter, cnt in sorted_dict:
            if letter.isalpha():
                print(f"{letter}: {cnt}")

        print(f"============= END ===============")

if __name__ == "__main__":
    main()

