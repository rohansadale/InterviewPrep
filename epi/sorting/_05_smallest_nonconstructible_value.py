def smallest_nonconstructible_value(arr):
    arr.sort()
    max_constructible = 0
    for x in arr:
        if x <= max_constructible+1:
            max_constructible += x
        else:
            break
    return max_constructible+1

if __name__ == "__main__":
    arr = [1,1,1,1,1,5,10,25]
    print "Array -", arr
    print "Smallest nonconstructible value =", smallest_nonconstructible_value(arr)