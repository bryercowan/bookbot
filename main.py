import sys
from stats import get_word_count, get_letter_count, sorted_letter_list


def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    text = get_book_text(sys.argv[1])
    words = get_word_count(text)
    letters = get_letter_count(text)
    sorted_letters = sorted_letter_list(letters)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {words} total words")
    print("--------- Character Count -------")
    for sl in sorted_letters:
        if sl["char"].isalpha():
            print(f"{sl['char']}: {sl['num']}")

    print("============= END ===============")
main()
