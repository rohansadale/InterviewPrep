def isclose(a, b, rel_tol=1e-09, abs_tol=0.0):
    return abs(a-b) <= max(rel_tol * max(abs(a), abs(b)), abs_tol)

def real_square_root(x):
    left, right = (0, 1.0) if x<1.0 else 1.0, x
    while not isclose(left, right):
        mid = (left+right)*0.5
        mid_square = mid * mid 
        if mid_square > x:
            right = mid
        else:
            left = mid
    return left

if __name__=="__main__":
    x = 6.25
    print "Square-root of", x, "is", real_square_root(x)
    x = 1
    print "Square-root of", x, "is", real_square_root(x)