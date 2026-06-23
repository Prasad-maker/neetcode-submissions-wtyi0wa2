class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        prefixsum = {0:1}
        cursum = 0
        for num in nums:
            cursum +=num
            diff = cursum - k
            res+=prefixsum.get(diff,0)
            prefixsum[cursum]=prefixsum.get(cursum,0)+1
        return res
        
        