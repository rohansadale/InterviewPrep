def binary_search(arr, x):
    left, right = 0, len(arr)-1
    while left <= right :
        mid = left + (right - left)/2
        if arr[mid] == x :
            return True
        if arr[mid] < x :
            left = mid+1
        else:
            right = mid-1
    return False

# Method 1 (Using binary search)
def intersect_two_sorted_arrays_binsearch(arr1, arr2):
    l1, l2 = len(arr1), len(arr2)

    # Keep arr1 smaller than arr2
    if l1 > l2:
        arr1, arr2 = arr2, arr1
        l1, l2 = l2, l1
    
    output = []
    for idx, x in enumerate(arr1):        
        if binary_search(arr2, x) and \
           (idx == 0 or output[-1] != x):
            output.append(x)
    return output

# Method 2
def intersect_two_sorted_arrays (arr1, arr2):
    ouput = []
    idx1, idx2 = 0, 0
    while idx1 < len(arr1) and idx2 < len(arr2):
        if arr1[idx1] == arr2[idx2]:
            if idx1 == 0 or arr1[idx1-1] != arr1[idx1]:
                ouput.append(arr1[idx1])
            idx1, idx2 = idx1+1, idx2+1
        elif arr1[idx1] < arr2[idx2]:
            idx1 += 1
        else:
            idx2 += 1
    return ouput

if __name__ == "__main__":
    arr1 = [2,3,3,5,5,6,7,7,8,12]
    arr2 = [5,5,6,8,8,9,10,10]
    print "Array1 -", arr1
    print "Array2 -", arr2
    print "Intersection of arrays (Binary search method) -", intersect_two_sorted_arrays_binsearch(arr1, arr2)
    print "Intersection of arrays -", intersect_two_sorted_arrays(arr1, arr2)
