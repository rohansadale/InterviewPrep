from stack import *

class MinStack(Stack):
    def __init__(self):
        self.top = None
        self.min_stack = []
    
    def push(self,x):
        temp = Node(x)
        if self.top:
            temp.next = self.top
        self.top = temp
        if not self.min_stack:
            self.min_stack.append(temp.val)
        elif temp.val <= self.min_stack[-1]:
            self.min_stack.append(temp.val)

    def pop(self):
        if not self.top:
            print "Nothing to pop. Stack is empty"
            return
        x = self.top.val
        self.top = self.top.next
        if self.min_stack[-1] == x:
            self.min_stack.pop()
        return x
    
    def get_min(self):
        if self.min_stack:
            return self.min_stack[-1]
        return -1

if __name__ == "__main__":
    s = MinStack()
    n = 5
    for i in range(n,-1,-1):
        s.push(i*i)
    print "Length of stack is ", len(s)
    print "Elements in stack are ", s
    print "Min in stack is ", s.get_min()
    for i in range(len(s)-2):
        print "Popping stack - ", s.pop()
    print "Elements in stack are ", s
    print "Min in stack is ", s.get_min()
    