import sys
from stats import count_words, count_characters

def report(book_path: str):
    print("============ BOOKBOT ============")
    with open(book_path) as f:
        content = f.read()
        print(f"Analyzing book found at {book_path}...")
        print("----------- Word Count ----------")
        print(f"Found {count_words(content)} total words")
        print("--------- Character Count -------")
        count_characters(content)
    print("============= END ===============")



def main():

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    report(book_path=sys.argv[1])
        # count_words(content) # 77986



main()