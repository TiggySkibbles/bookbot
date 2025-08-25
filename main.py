import sys
from stats import count_words, count_characters, sort_dict

def get_book_text(book_path: str) -> str:
    with open(f"{book_path}", "r", encoding="utf-8") as file:
        return file.read()

def generate_report(path: str) -> tuple[str, int, dict]:
    book = get_book_text(path)
    num_words = count_words(book)
    num_characters = count_characters(book)
    sorted_characters = sort_dict(num_characters)
    print(f"{num_words} words found in the document.")
    return path, num_words, sorted_characters

def main(path: str) -> None:
    book, num_words, sorted_characters = generate_report(path)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at: {book}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("------- Character Count ---------")
    for char in sorted_characters:
        if char.isalpha():
            print(f"{char}: {sorted_characters[char]}")
    print("============= END ===============")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        exit(1)
    main(sys.argv[1])