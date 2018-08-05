from stack import *

class MyQueue:
    def __init__(self):
        self.s1 = Stack()
        self.s2 = Stack()
    
    def push(self, x):
        self.s1.push(x)
    
    def pop(self):                    
        if not self.s2:
            while self.s1.top:
                self.s2.push(self.s1.top.val)
                self.s1.top = self.s1.top.next
        x = self.s2.pop()
        return x
    
    def __str__(self):
        temp = self.s1.top
        arr = []
        while temp:
            arr.append(temp.val)
            temp = temp.next
        temp = self.s2.top
        while temp:
            arr.append(temp.val)
            temp = temp.next        
        return str(arr)

if __name__ == "__main__":
    q = MyQueue()
    for i in range(5):
        q.push(i*i)    
    print "Elements in stack are ", q
    for i in range(2):
        print "Popping stack - ", q.pop()
    q.push(100)
    print "Elements in stack are ", q
    q.pop()
    print "Elements in stack are ", q