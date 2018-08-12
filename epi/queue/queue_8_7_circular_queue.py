import random

class Queue:
    SCALE_FACTOR = 2

    def __init__(self, capacity):
        self._data = [None]*capacity
        self.head = self.tail = self._num_of_elem = 0
    
    def enqueue(self, x):        
        if self._num_of_elem == len(self._data):
            # Need to resize
            self._data = self._data[self.head:] + self._data[:self.head]
            self._data += [None] * (Queue.SCALE_FACTOR * len(self._data) - len(self._data))
            self.head = 0
            self.tail = self._num_of_elem
            
        self._data[self.tail] = x
        self.tail = (self.tail + 1)%len(self._data)
        self._num_of_elem += 1
    
    def dequeue(self):
        if not self._num_of_elem:
            raise IndexError("Empty Queue")
        self._num_of_elem -= 1
        result = self._data[self.head]
        self.head = (self.head + 1)% len(self._data)
        return result
    
    def __len__(self):
        return self._num_of_elem    

if __name__ == "__main__":
    q = Queue(3)
    for _ in range(3):
        x = random.choice(range(100))
        print "Adding to queue - ", x
        q.enqueue(x)
    print len(q)
    for _ in range(1):
        print "Dequeue element - ", q.dequeue()
    print "Adding to queue - 100"
    q.enqueue(100) 
    print len(q)