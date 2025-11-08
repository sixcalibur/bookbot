import sys

from stats import get_num_letters, get_num_words, sort_dict


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    text = get_book_text(book_path)
    words = get_num_words(text)
    letters: dict[str, int] = get_num_letters(text)
    sorted = sort_dict(letters)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {words} total words")
    print("--------- Character Count -------")
    for x in sorted:
        print(f"{x['char']}: {x['num']}")
    print("============= END ===============")


def get_book_text(path: str):
    with open(path) as f:
        return f.read()


main()
