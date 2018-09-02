import collections

def smallest_seq_subset(paragraph, keywords):
    # hash map of keywords
    keyword_to_idx_map = {word: idx for idx, word in enumerate(keywords)}
    # list to keep track of latest occurrence of each keyword
    latest_occurence = [-1] * len(keywords)
    # list to keep track of length of shortest subarray till that keyword
    shortest_subarr_len = [float('inf')] * len(keywords)

    shortest_dist = float('inf')
    result = [-1, -1]

    for idx, word in enumerate(paragraph):
        if word in keyword_to_idx_map:
            keyword_idx = keyword_to_idx_map[word]
            # Start the matching when we see first keyword
            if keyword_idx == 0:
                shortest_subarr_len[keyword_idx] = 1
            # For second keyword onwards,
            # Get distance to latest  occurence of prev keyword
            # Calculate the subarray length till this keyword
            elif shortest_subarr_len[keyword_idx - 1] != float('inf'):
                distance_to_prev_keyword = idx - \
                                    latest_occurence[keyword_idx-1]
                shortest_subarr_len[keyword_idx] = distance_to_prev_keyword + \
                                    shortest_subarr_len[keyword_idx - 1]
            # Update the latest occurence of keyword
            latest_occurence[keyword_idx] = idx

            # If we reach the last keyword,
            # Calculate shortest distance for comparison
            # Calculate left and right indices.
            if keyword_idx == len(keywords)-1 and \
                    shortest_subarr_len[-1] < shortest_dist:
                shortest_dist = shortest_subarr_len[-1]
                result = [idx - shortest_dist + 1, idx]
    return result

if __name__ == "__main__":
    paragraph = "apple banana cat apple"
    paragraph = paragraph.split()
    keywords = ["banana", "apple"]
    print "Paragraph -", paragraph
    print "Keywords -", keywords
    print "Left and right index of shortest subarray =", smallest_seq_subset(paragraph, keywords)
