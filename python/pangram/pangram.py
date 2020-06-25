def is_pangram(sentence):
    tag=True
    a_pangram='thequickbrownfoxjumpsoverthelazydog'
    for char in a_pangram:
        if char not in sentence.lower():
            tag = False
            break
    return tag
