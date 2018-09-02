def test_palindrome(word):
    letter_map = {}
    for char in word:
        if char in letter_map:
            letter_map[char] += 1
        else:
            letter_map[char] = 1
    _sum = 0
    for cnt in letter_map.values():
        _sum += (cnt%2)
    return _sum<=1

if __name__ == "__main__":
    word = "edified"
    print test_palindrome(word)
    word = "rohan"
    print test_palindrome(word)