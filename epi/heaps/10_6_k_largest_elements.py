import heapq

def k_largest_binary_heap(arr, k):
    if k <= 0:
        return []
    
    result, candidate_max_heap = [], []
    candidate_max_heap.append((-arr[0],0))
    for _ in range(k):
        candidate_idx = candidate_max_heap[0][1]
        result.append(-heapq.heappop(candidate_max_heap)[0])
        l_child_idx = 2*candidate_idx+1
        if l_child_idx < len(arr):
            heapq.heappush(candidate_max_heap, (-arr[l_child_idx], l_child_idx))
        r_child_idx = 2*candidate_idx+2
        if r_child_idx < len(arr):
            heapq.heappush(candidate_max_heap, (-arr[r_child_idx], r_child_idx))
    return result

if __name__ == "__main__":
    arr = [561, 314, 401, 28, 156, 359, 271, 11, 1]
    print k_largest_binary_heap(arr, 4)