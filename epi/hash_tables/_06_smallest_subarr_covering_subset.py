import collections

def smallest_subarr_covering_set(paragraph, keywords):
    result = [-1, -1]
    left = 0

    # map to keep count of keywords
    keyword_count = collections.Counter(keywords)
    # number of keywords left to process
    remaining_words = len(keywords)

    for right, word in enumerate(paragraph):
        # increment right till we cover all keywords
        if word in keyword_count:
            keyword_count[word] -= 1
            if keyword_count[word] == 0:
                remaining_words -= 1
        
        # when all keywords are covered,
        # calculate left and right index if it's less than previously calculated diff
        while remaining_words == 0:
            if (result == [-1, -1]) or (right-left < result[1]-result[0]):
                result = [left, right]
            # set pointer to left (first element where remaining_words was 0)
            # eg. for first hit, [apple banana apple apple dog cat] left = 0, right = 5
            pl = paragraph[left]

            # increment left till we find first keyword
            # this will set left and right indices correctly
            # eg. for first hit, [banana apple apple dog cat] left = 1, right = 5
            if pl in keyword_count:
                keyword_count[pl] += 1
                remaining_words += 1
            left += 1
    return result

if __name__ == "__main__":
    paragraph = "apple banana apple apple dog cat apple dog banana apple cat dog"
    paragraph = paragraph.split()
    keywords = ["banana", "cat"]
    print "Paragraph -", paragraph
    print "Keywords -", keywords
    print "Left and right index of shortest subarray =", smallest_subarr_covering_set(paragraph, keywords)
