class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minheap = [-i for i in nums]
        res = 0
        heapq.heapify(minheap)
        while k>0:
            res = heapq.heappop(minheap)
            k-=1
        return -res

        