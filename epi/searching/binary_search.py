def binary_search(arr, x):
    left, right = 0, len(arr)-1
    while left <= right :
        mid = left + (right - left)/2
        if arr[mid] == x :
            return mid
        if arr[mid] < x :
            left = mid+1
        else:
            right = mid-1
    return -1

if __name__=="__main__":
    arr = [-14, -10, 2, 108, 243, 285]
    x = 24
    print binary_search(arr, x)