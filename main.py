from collections import defaultdict

def count_words(content: str):
    print(f"{len(content.split())} words found in the document")


def count_characters(content: str):
    counter = defaultdict(int)
    for ch in content:
        if ch.lower().isalnum():
            counter[ch.lower()] += 1
    for ch, amount in counter.items():
        print(f"The '{ch}' character was found {amount} times")
        

def report():
    with open('books/frankenstein.txt') as f:
        content = f.read()
        print("--- Begin report of books/frankenstein.txt ---")
        count_words(content)
        count_characters(content)
        print('--- End report ---')



def main():
    report()
        # count_words(content) # 77986



main()