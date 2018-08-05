def remove_dup_1(word):
    arr = list(word)
    n = len(arr)
    new_i = 0
    for i in range(n):
        j = 0
        while j < i:
            if arr[i] == arr[j]:
                break
            j += 1
        if i == j:
            arr[new_i] = arr[i]
            new_i += 1
    return ''.join(arr[:new_i])

def remove_dup_2(word):
    arr = list(word)
    new_i = 0
    # 256 ASCII characters
    hit = [0]*256
    n = len(arr)
    for i in range(n):
        val = ord(arr[i])
        if hit[val]==0:
            hit[val] = 1
            arr[new_i] = arr[i]
            new_i += 1
    return ''.join(arr[:new_i])

word = "aaadac"
#print remove_dup_1(word)
print remove_dup_2(word)
