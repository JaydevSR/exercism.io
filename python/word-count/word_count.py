import re

def count_words(sentence: str):
    sentence = sentence.lower()
    words = map(lambda x: x.strip("'"), filter(None, re.split("[^a-zA-Z0-9']", sentence)))
    word_dict = dict()
    for word in words:
        word_dict[word] = word_dict.get(word, 0) + 1
    return word_dict