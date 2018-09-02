def longest_subarr_distinct_elem(arr):
    most_recent_occurence = {}
    longest_dup_free_idx = 0
    result = 0
    for idx, x in enumerate(arr):
        if x in most_recent_occurence:
            dup_idx = most_recent_occurence[x]
            if dup_idx >= longest_dup_free_idx:
                result = max(result, idx - longest_dup_free_idx)
                longest_dup_free_idx = dup_idx + 1
        most_recent_occurence[x] = idx

    # If all elements are distinct or last x elements subarr is longest
    return max(result, len(arr) - longest_dup_free_idx)

if __name__ == "__main__":
    word = "fsfetwenwe"
    arr = list(word)
    print "Array =", arr
    print "Length of longest subarray with distinct elements =", longest_subarr_distinct_elem(arr)