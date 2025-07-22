import heapq
def kth_smallest(matrix, k):
    n = len(matrix)
    min_heap = []
    for i in range(min(k, n)):
        heapq.heappush(min_heap, (matrix[i][0], i, 0))
    count = 0
    while min_heap:
        val, r, c = heapq.heappop(min_heap)
        count += 1
        if count == k:
            return val
        if c + 1 < n:
            heapq.heappush(min_heap, (matrix[r][c + 1], r, c + 1))
matrix=[[1, 5, 9],
        [10, 11, 13],
        [12, 13, 15]]
k = 8
print(f"{k}th smallest element is:", kth_smallest(matrix, k))
