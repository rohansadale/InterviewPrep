def longest_contained_interval(arr):
    unprocessed_entries = set(arr)
    max_interval_size = 0
    while unprocessed_entries:
        x = unprocessed_entries.pop()
        lower_bound = x-1
        while lower_bound in unprocessed_entries:
            unprocessed_entries.remove(lower_bound)
            lower_bound -= 1
        upper_bound = x+1
        while upper_bound in unprocessed_entries:
            unprocessed_entries.remove(upper_bound)
            upper_bound += 1
        max_interval_size = max(max_interval_size, upper_bound - lower_bound -1)
    return max_interval_size

if __name__ == "__main__":
    arr = [10, 5, 3, 11, 6, 100, 4]
    print "Array =", arr
    print "Longest contained interval =", longest_contained_interval(arr)