from stack import *
import random

def sort_stack(s):
    r = Stack()
    while s:
        temp = s.pop()        
        while r and temp<r.peek():
            s.push(r.pop())
        r.push(temp)
    return r

if __name__ == "__main__":
    s = Stack()
    for i in range(5):
        s.push(random.choice(range(10)))
    print "Elements in stack are ", s
    print sort_stack(s)