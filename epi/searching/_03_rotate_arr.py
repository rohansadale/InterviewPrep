def search_smallest(arr):
    left, right = 0, len(arr)-1
    while left < right:
        mid = (left+right)/2
        if arr[mid] < arr[right]:
            right = mid
        else:
            left = mid+1
    return arr[left]

if __name__=="__main__":
    arr = [378, 478, 631, 279, 368]
    print "Elements in array =", arr
    print "Smallest element =", search_smallest(arr)