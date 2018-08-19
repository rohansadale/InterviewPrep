import heapq

def sort_almost_sorted_arr(arr, k):
    result, min_heap = [], []
    for i in range(k):
        heapq.heappush(min_heap, arr[i])    
    for i in range(k, len(arr)):
        x = heapq.heappop(min_heap)
        result.append(x)
        heapq.heappush(min_heap, arr[i])
    while min_heap:
        result.append(heapq.heappop(min_heap))
    return result

if __name__=="__main__":
    arr = [3, -1, 2, 6, 4, 5, 8]
    print sort_almost_sorted_arr(arr, 2)