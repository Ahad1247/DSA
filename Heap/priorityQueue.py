import heapq

arr = [1,4,3,6,2]

pq = []

heapq.heappush(pq,2)
heapq.heappush(pq,4)
heapq.heappush(pq,5)
heapq.heappush(pq,7)
heapq.heappush(pq,1)
heapq.heappop(pq)
heapq.heappop(pq)
heapq.heappop(pq)

heapq.heapify(arr)

print(arr)