def is_rotated(word1, word2):
    word2 = word2 + word2
    if word1 in word2:
        return True
    return False

word1 = "apple"
#word2 = "pleap"
word2 = "ppale"
print is_rotated(word1, word2)
