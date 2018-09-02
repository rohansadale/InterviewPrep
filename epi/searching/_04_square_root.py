def square_root(x):
    left, right = 0, x
    while left <= right:
        mid = (left+right)/2
        mid_square = mid * mid
        if mid_square == x:
            return mid
        elif mid_square < x:
            left = mid+1
        else:
            right = mid-1
    return left-1

if __name__=="__main__":
    x = 300
    print "Square-root of", x, "is", square_root(x)
    x = 144
    print "Square-root of", x, "is", square_root(x)