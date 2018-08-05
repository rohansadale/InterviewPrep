def set_zeros_in_matrix(arr):
    m = len(arr)
    n = len(arr[0])
    rows = [0]*m
    columns = [0]*n

    for i in range(m):
        for j in range(n):
            if arr[i][j] == 0:
                rows[i] = 1
                columns[i] = 1
    for i in range(m):
        for j in range(n):
            if rows[i] or columns[j]:
                arr[i][j] = 0
    return arr

arr = [[1,0,1], [1,1,1], [2,3,4]]
print set_zeros_in_matrix(arr)
