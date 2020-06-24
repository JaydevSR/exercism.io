function acronym(phrase)
    word_list = split(phrase, r"[^A-Za-z0-9']+")
    return join([uppercase(word[1]) for word in word_list])
end
