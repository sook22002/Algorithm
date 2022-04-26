import heapq
s = [1, 2, 3, 9, 10, 12]
k = 7
def solution(scoville, k):
    heap = []

    for num in scoville:
        heapq.heappush(heap, num)
  
    mix_cnt = 0

    while heap[0] < k:
        try:
            heapq.heappush(heap, heapq.heappop(heap) + (heapq.heappop(heap) * 2))
        except IndexError:
             return -1
        mix_cnt += 1
 
    return mix_cnt

print(solution(s, k))
a = 0