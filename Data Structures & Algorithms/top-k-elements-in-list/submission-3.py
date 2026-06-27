class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for num in nums:
            count[num]+=1
        minheap = []
        for n,c in count.items():
            heapq.heappush(minheap,(c,n))
            if len(minheap)>k:
                heapq.heappop(minheap)
        res = []
        for _,n in minheap:
            res.append(n)
        return res