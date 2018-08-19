class MinHeap:
    def __init__(self):
        self.current_size = 0
        self.heap = [0]
    
    def insert(self, x):
        self.current_size += 1
        self.heap.append(x)
        self.perc_up(self.current_size)
    
    def perc_up(self, idx):
        while idx // 2:
            if self.heap[idx] < self.heap[idx // 2]:
                self.heap[idx], self.heap[idx // 2] = self.heap[idx // 2], self.heap[idx]
            idx //= 2
        
    def delete(self):
        x = self.heap[self.current_size]        
        self.heap[1] = self.heap[self.current_size]
        self.current_size -= 1
        self.heap.pop()
        self.perc_down(1)
        return x
    
    def perc_down(self, idx):
        while idx*2 <= self.current_size:
            i = self.min_child(idx)
            if self.heap[idx] > self.heap[i]:
                self.heap[idx], self.heap[i]  = self.heap[i], self.heap[idx]
            idx = i
    
    def min_child(self, i):
        if i*2+1 > self.current_size:
            return i*2
        if self.heap[i*2] < self.heap[i*2+1]:
            return i*2
        return i*2+1
    
    def build_heap(self, arr):
        idx = len(arr)//2
        self.heap += arr
        self.current_size = len(arr)
        while idx > 0:
            self.perc_down(idx)
            idx -= 1
    
    def get_min(self):
        if self.current_size:
            return self.heap[1]
        raise IndexError("No elements in heap")

    def _print(self):
        print self.heap[1:]


if __name__ == "__main__":
    h = MinHeap()
    arr = [9, 6, 5, 2, 3]
    print "Initial array -", arr
    h.build_heap(arr)
    print "After heapify -", 
    h._print()
    print "Inserting 7 to heap .." 
    h.insert(7)
    print "Inserting 1 to heap .." 
    h.insert(1)
    print "Current heap -",
    h._print()
    print "Deleting min element -", h.get_min() 
    h.delete()
    print "Current heap -",
    h._print()
