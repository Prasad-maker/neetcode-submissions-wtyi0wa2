class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums==[]:
            return 0
        maxseq = 1
        hmap = set(nums)
        for n in nums:
            if n-1 not in hmap:
                cur = 1
                k=n+1
                while k in hmap:
                    cur+=1
                    k+=1
                maxseq=max(maxseq,cur)
                
            
        return maxseq
        