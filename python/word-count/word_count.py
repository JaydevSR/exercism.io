import re
from collections import Counter

def count_words(sentence: str):
    sentence = sentence.lower()
    words = map(lambda x: x.strip("'"), filter(None, re.split("[^a-zA-Z0-9']", sentence)))
    return dict(Counter(words))