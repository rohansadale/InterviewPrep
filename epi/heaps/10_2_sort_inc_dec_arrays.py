import heapq

# From 10_1_merge_sorted_arrays.py
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

def sort_increasing_decreasing_array(arr):
    sorted_arrays = []
    INCREASING, DECREASING = 0, 1
    subarr_type = INCREASING
    start_idx = 0
    for i in range(1, len(arr)+1):
        if (i==len(arr)) or \
           (arr[i-1] < arr[i] and subarr_type==DECREASING) or \
           (arr[i-1] > arr[i] and subarr_type==INCREASING):
            temp_arr = []
            if subarr_type == INCREASING:
                temp_arr = arr[start_idx:i]
                subarr_type = DECREASING
            else:
                temp_arr = arr[i-1 : start_idx-1 : -1]
                subarr_type = INCREASING
            sorted_arrays.append(temp_arr)
            start_idx = i
    return merge_sorted_arrays(sorted_arrays)

if __name__=="__main__":
    arr = [57, 131, 493, 294, 221, 339, 418, 452, 442, 190]
    print sort_increasing_decreasing_array(arr)