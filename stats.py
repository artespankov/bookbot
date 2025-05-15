from collections import defaultdict
def count_words(content: str):
    return len(content.split())

def count_characters(content: str):
    counter = defaultdict(int)
    for ch in content:
        if ch.lower().isalnum():
            counter[ch.lower()] += 1
    for ch, amount in counter.items():
        print(f"{ch}: {amount}")
