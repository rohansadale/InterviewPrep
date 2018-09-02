import collections


def find_all_substrings(s, words):

    # function to match the smaller set to complete sentence
    def match_all_words_in_dict(start):
        cur_word_freq = collections.Counter()
        for i in range(start, start+len(words)*word_len, word_len):
            cur_word = s[i: i+word_len]
            it = words_cnt[cur_word]
            if it == 0:
                return False
            cur_word_freq[cur_word] += 1
            if cur_word_freq[cur_word] > it:
                return False
        return True

    # Map to keep word precense and count
    words_cnt = collections.Counter(words)
    # Since all words are of same length
    word_len = len(words[0])
    output = []
    for i in range(len(s) - len(words)*word_len + 1):        
        if match_all_words_in_dict(i):
            output.append(s[i:i+len(words)*word_len])
    return output

if __name__ == "__main__":
    sentence = "amanaplanacanapl"
    words = ["can", "apl", "ana"]
    print "Sentence -", sentence
    print "Words -", words
    print "Word concatenation found in sentence -", find_all_substrings(sentence, words)
