class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap = {}
        for num in nums:
            hmap[num]=hmap.get(num,0)+1
        arr = [(-hmap[i],i) for i in hmap.keys()]
        heapq.heapify(arr)
        res =[]
        for i in range(k):
            res.append(heapq.heappop(arr)[1])
        return res

        