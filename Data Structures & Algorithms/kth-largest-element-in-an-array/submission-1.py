class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minheap = list(nums[:k])
        heapq.heapify(minheap)
        for n in nums[k:]:
            if minheap[0]<n:
                heapq.heappush(minheap,n)
                heapq.heappop(minheap)
        return minheap[0]


        