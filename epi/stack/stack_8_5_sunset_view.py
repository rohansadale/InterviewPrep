def sunset_view(arr):
    sunset_stack = []
    for _, val in enumerate(arr):
        while sunset_stack and val >= sunset_stack[-1]:
            sunset_stack.pop()
        sunset_stack.append(val)
    return sunset_stack

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    print "Sunset view available for buildings in", arr, " are", sunset_view(arr)

    arr.reverse()
    print "Sunset view available for buildings in", arr, " are", sunset_view(arr)
    
    arr = [1, 3, 5, 4, 2]
    print "Sunset view available for buildings in", arr, " are", sunset_view(arr)
