class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = {}
        for n in nums:
            buckets[n] = buckets.get(n,0)+1
        arr = [(buckets[x],x)for x in buckets]
        arr.sort(reverse=True)
        res = []
        for i in range(k):
            res.append(arr[i][1])
        return res


        