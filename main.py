import sys
from stats import count_words, count_chars, generate_report

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    book_path = sys.argv[1]

def get_book_text(book_path):
    with open(book_path) as f:
        file_contents = f.read()
        return file_contents

def main():
    book_text = get_book_text(book_path)
    wc = count_words(book_text)
    char_count = count_chars(book_text)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {wc} total words")
    print("--------- Character Count -------")
    for entry in generate_report(char_count):
        print(f"{entry['char']}: {entry['num']}")
    # print(generate_report(char_count))



    print("============= END ===============")

main()

