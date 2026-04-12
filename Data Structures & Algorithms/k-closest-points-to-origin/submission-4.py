class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for i in range(k):
            p=points[i]
            heap.append((-p[0]*p[0]-p[1]*p[1],p))
        heapq.heapify(heap)
        for p in points[k:]:
            dis = -p[0]*p[0]-p[1]*p[1]
            if dis>heap[0][0]:
                heapq.heappop(heap)
                heapq.heappush(heap,(-dis,p))
        return [i[1] for i in heap]
        

        