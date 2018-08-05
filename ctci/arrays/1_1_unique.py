
# Space - 256 ASCII charater set
def is_unique_1(word):
    arr = [0]*256
    for ch in word:
        val = ord(ch)
        if arr[val]:
            return False
        arr[val] = 1
    return True

# using bitwise operator
def is_unique_2(word):
    checker = 0
    for ch in word:
        val = ord(ch) - ord('a')
        if checker and 1<<val:
            return False
        checker = checker | (1<<val)
    return True

word = "Rohano"
print is_unique_1(word)
print is_unique_2(word)
