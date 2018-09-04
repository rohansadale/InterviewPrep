def merge_sorted_arrays (arr1, l1, arr2, l2):
    a, b, merge_idx = l1-1, l2-1, l1+l2-1
    while a>=0 and b>=0:
        if arr1[a] > arr2[b]:
            arr1[merge_idx] = arr1[a]
            a -= 1
        else:
            arr1[merge_idx] = arr2[b]
            b -= 1
        merge_idx -= 1
    while b >= 0:
        arr1[merge_idx] = arr2[b]
        b -= 1
        merge_idx -= 1
    return arr1

if __name__ == "__main__":
    arr1 = [3,13,17]
    l1 = len(arr1)
    arr2 = [3,7,11,19]
    l2 = len(arr2)
    arr1 += [None]*len(arr2)
    print "Merging arrays -", arr1[:l1], arr2
    print "Output -", merge_sorted_arrays(arr1, l1, arr2, l2)