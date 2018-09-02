import collections

def is_letter_constructible_from_magazine(letter, magazine):
    letter_counter = collections.Counter(letter)
    for char in magazine:
        if char in letter_counter:
            letter_counter[char] -= 1
            if letter_counter[char] == 0:
                del letter_counter[char]
    return not letter_counter

if __name__ == "__main__":
    letter = "I am Ro."
    magazine = "Rohan is good. I am Groot."
    print "Letter -", letter
    print "Magazine -", magazine
    print is_letter_constructible_from_magazine(letter, magazine)