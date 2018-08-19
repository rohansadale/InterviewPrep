import heapq

def online_median(sequence):
    min_heap, max_heap, result = [], [], []
    for x in sequence:
        heapq.heappush(min_heap, x)
        temp_elem = heapq.heappop(min_heap)
        if temp_elem is not None:
            heapq.heappush(max_heap, -temp_elem)        
        if len(max_heap) > len(min_heap):
            heapq.heappush(min_heap, -heapq.heappop(max_heap))
        median = None
        if len(max_heap) == len(min_heap):
            median = 0.5 * (min_heap[0] + -max_heap[0])
        else:
            median = min_heap[0]
        result.append(median)
        #print x, min_heap, max_heap, median
    return result

if __name__=="__main__":
    arr = [1, 0, 3, 5, 2, 0, 1]
    print "Initial array -", arr
    print "Online median -", online_median(arr)