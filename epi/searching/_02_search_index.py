def search_entry_equal_to_idx(arr):
    left, right = 0, len(arr)-1
    while left <= right:
        mid = (left + right)/2
        if arr[mid] == mid:
            return mid
        if arr[mid] < mid:
            left = mid+1
        else:
            right = mid-1
    return -1

if __name__ == "__main__":
    arr = [-2, 0, 2, 3, 6, 7, 9]
    print "Elements in array -", arr
    print search_entry_equal_to_idx(arr)