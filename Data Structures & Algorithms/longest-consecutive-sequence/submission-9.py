class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hmap = defaultdict(int)
        maxseq = 0
        for n in nums:
            if not hmap[n]:
                hmap[n]=hmap[n-1]+hmap[n+1]+1
                hmap[n-hmap[n-1]]=hmap[n]
                hmap[n+hmap[n+1]]=hmap[n]
                maxseq = max(maxseq,hmap[n])
            
        return maxseq
        