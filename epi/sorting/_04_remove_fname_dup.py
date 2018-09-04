class Name:
    def __init__(self, first, last):
        self.first = first
        self.last = last
    
    def __eq__(self, other):        
        return self.first == other.first
    
    def __lt__(self, other):
        if self.first != other.first:
            return self.first < other.first
        else:
            return self.last < other.last

def eliminate_duplicates(arr):
    arr.sort()    
    write_idx = 1
    for name in arr[1:]:      
        if not (name == arr[write_idx-1]):
            arr[write_idx] = name
            write_idx += 1
    del arr[write_idx:]
    for name in arr:
        print name.first, name.last
    return arr

if __name__ == "__main__":
    arr =  [
        Name("Ian", "Botham"),
        Name("David", "Gower"),
        Name("Ian", "Bell"),
        Name("Ian", "Chappell")        
    ]
    print "Initial array list - "
    for name in arr:
        print name.first, name.last
    print "\nEliminating first name duplicates -"
    eliminate_duplicates(arr)
