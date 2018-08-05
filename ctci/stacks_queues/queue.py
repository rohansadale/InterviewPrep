class Node:
    def __init__(self, x):
        self.val = x
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
    
    def enqueue(self, x):
        temp = Node(x)
        if not self.front:
            self.front = temp
            self.rear = temp
        else:
            self.rear.next = temp
            self.rear = self.rear.next
    
    def dequeue(self):
        if not self.front:
            print "Nothing to dequeue. Queue is empty."
        x = self.front.val
        if self.front == self.rear:
            self.front = None
            self.rear = None
        else:
            self.front = self.front.next
        return x
    
    def __str__(self):
        temp = self.front
        arr = []
        while temp:
            arr.append(temp.val)
            temp = temp.next
        return str(arr)
    
    def __len__(self):
        temp = self.front
        cnt = 0
        while temp:
            cnt += 1
            temp = temp.next
        return cnt

if __name__=="__main__":
    q = Queue()
    for i in range(5):
        q.enqueue(i*i*i)
    print "Length of Queue is ", len(q)
    print "Elements in Queue are ", q
    for i in range(len(q)-2):
        print "Dequeue - ", q.dequeue()
    print "Elements in Queue are ", q