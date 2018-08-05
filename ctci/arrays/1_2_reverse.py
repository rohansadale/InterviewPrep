def reverse(word):
    arr = list(word)
    low = 0
    high = len(arr)-1
    while low < high:
        arr[low], arr[high] = arr[high], arr[low]
        low += 1
        high -= 1
    return ''.join(arr)

word = "abcde"
print reverse(word)
