def find_anagrams(word, candidates):
    anagrams = [
                i for i in candidates 
                if all([
                        word.lower() != i.lower(),
                        sorted(i.lower()) == sorted(word.lower()),
                    ])
                ]
    return anagrams