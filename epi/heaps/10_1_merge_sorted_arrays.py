import heapq
from min_heap import MinHeap

def merge_sorted_arrays(sorted_arrays):
    min_heap = []
    sorted_arr_iter = [iter(x) for x in sorted_arrays]

    # push first element from each arr
    for i, it in enumerate(sorted_arr_iter):
        element = next(it, None)
        heapq.heappush(min_heap, (element, i))
    
    result = []
    while min_heap:
        min_elem, min_elem_idx = heapq.heappop(min_heap)
        min_arr_iter = sorted_arr_iter[min_elem_idx]
        result.append(min_elem)
        next_elem = next(min_arr_iter, None)
        if next_elem is not None:
            heapq.heappush(min_heap, (next_elem, min_elem_idx))
    return result

if __name__ == "__main__":
    sorted_arrays = [
        [1, 3, 5, 7],
        [2, 4, 6, 8],
        [0, 9, 10, 11]
    ]
    print merge_sorted_arrays(sorted_arrays)