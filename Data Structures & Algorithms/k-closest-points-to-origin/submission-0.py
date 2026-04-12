class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minheap = []
        res = []
        for p in points:
            minheap.append([p[0]*p[0]+p[1]*p[1],p[0],p[1]])
        heapq.heapify(minheap)
        if len(points)<=k:
            return points
        while(k>0):
            point = heapq.heappop(minheap)
            res.append([point[1],point[2]])
            k-=1
        return res

        