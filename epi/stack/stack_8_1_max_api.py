import random

class Stack:
    class MaxWithCount:
        def __init__(self, max, count):
            self.max = max
            self.count = count

    def __init__(self):
        self._element = []
        self._cache_max_count = []
    
    def is_empty(self):
        return len(self._element)==0

    def push(self, x):
        self._element.append(x)
        if len(self._cache_max_count) == 0:
            self._cache_max_count.append(self.MaxWithCount(x, 1))
        elif self._cache_max_count[-1].max < x:
            self._cache_max_count.append(self.MaxWithCount(x, 1))
        elif self._cache_max_count[-1].max == x:
            self._cache_max_count[-1].count += 1         
    
    def pop(self):        
        if self.is_empty():
            return None
        x = self._element.pop()        
        if self._cache_max_count[-1].max == x:
            self._cache_max_count[-1].count -= 1
            if self._cache_max_count[-1].count == 0:
                self._cache_max_count.pop()
        return x
    
    def get_max(self):
        if not self.is_empty():
            return self._cache_max_count[-1].max

if __name__=="__main__":
    s = Stack()
    for _ in range(5):        
       s.push(random.choice(range(100)))
    # arr = [17, 25, 16, 91, 26]
    # for x in arr:
    #     s.push(x)
    print "Elements in stack - ", s._element
    print "Max element - ", s.get_max()    
    for _ in range(2):
        print "Popping element - ", s.pop()
    print "Elements in stack - ", s._element
    print "Max element - ", s.get_max()