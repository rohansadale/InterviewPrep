def find_anagrams(dictionary):
    anagrams = {}
    for word in dictionary:
        sorted_word = ''.join(sorted(word))        
        if sorted_word in anagrams.keys():
            anagrams[sorted_word].append(word)
        else:
            anagrams[sorted_word] = [word]
    output = []
    for val in anagrams.values():
        if len(val) > 1:
            output.append(val)
    return output

if __name__ == "__main__":
    dictionary=["debitcard", "elvis", "badcredit", "lives", "money", "levis"]
    print find_anagrams(dictionary)