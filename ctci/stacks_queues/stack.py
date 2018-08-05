class Node:
    def __init__(self, x):
        self.val = x
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
    
    def push(self, x):
        temp = Node(x)
        if self.top:
            temp.next = self.top
        self.top = temp
    
    def pop(self):
        if not self.top:
            print "Nothing to pop. Stack is empty"
            return
        x = self.top.val
        self.top = self.top.next
        return x

    def peek(self):
        if self.top:
            return self.top.val
            
    def __str__(self):
        temp = self.top
        arr = []
        while temp:
            arr.append(temp.val)
            temp = temp.next
        return str(arr)
        
    def __len__(self):
        temp = self.top
        cnt = 0
        while temp:
            cnt += 1
            temp = temp.next
        return cnt
        
if __name__ == "__main__":
    s = Stack()
    for i in range(5):
        s.push(i*i)
    print "Length of stack is ", len(s)
    print "Elements in stack are ", s
    for i in range(len(s)-2):
        print "Popping stack - ", s.pop()
    print "Elements in stack are ", s