def compute_h_index(arr):
    l = len(arr)
    arr.sort()
    for idx, val in enumerate(arr):
        if val >= l - idx:
            return l-idx
    return 0

if __name__ == "__main__":
    arr = [6,9,5,8,1]
    print "Array -", arr
    print "h-index =", compute_h_index(arr) 