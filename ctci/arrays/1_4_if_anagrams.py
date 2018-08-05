def if_anagrams(word1, word2):
    if len(word1) != len(word2):
        return False

    hit = [0]*256
    distinct_cnt = 0
    for ch in word1:
        val = ord(ch)
        if not hit[val]:
            distinct_cnt += 1
        hit[val] += 1
    cur_distinct_cnt = 0
    for ch in word2:
        val = ord(ch)   
        # Different character present in word2
        if hit[val] == 0:
            return False
        hit[val] -= 1
        if hit[val] == 0:
            distinct_cnt -= 1
    return distinct_cnt == 0

word1 = 'abad'
word2 = 'bcda'
print if_anagrams(word1, word2)
            
