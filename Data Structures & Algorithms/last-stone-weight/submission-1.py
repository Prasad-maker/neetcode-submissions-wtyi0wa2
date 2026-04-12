class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxheap = [-i for i in stones]
        heapq.heapify(maxheap)
        while(len(maxheap)>1):
            s1=-heapq.heappop(maxheap)
            s2=-heapq.heappop(maxheap)
            if s1!=s2:
                heapq.heappush(maxheap,s2-s1)
        return -maxheap[0] if maxheap else 0

        