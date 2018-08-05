def replace_spaces(words):
    new_word = ""
    for ch in words:
        if ch == ' ':
            new_word += "%20"
        else:
            new_word += ch
    return new_word

words = "I am Rohan Sadale "
print replace_spaces(words)
