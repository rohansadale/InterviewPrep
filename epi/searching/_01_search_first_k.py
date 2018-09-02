def search_first_k (arr, k):
    left, right, result = 0, len(arr)-1, -1
    while left <= right:
        mid = (left + right)/2
        if arr[mid] == k:
            result = mid
            right = mid-1
        elif arr[mid] < k:
            left = mid+1
        else:
            right = mid-1
    return result

if __name__ == "__main__":
    arr = [-14, -10, 2, 108, 108, 243, 285, 285, 401]
    x = 285
    print "Elements in array -", arr
    print "Search element -", x
    print search_first_k(arr, x)