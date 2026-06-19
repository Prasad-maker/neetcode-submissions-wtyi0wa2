class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum,cur = nums[0],0
        for num in nums:
            cur+=num
            maxsum = max(maxsum,cur)
            if cur<0:
                cur = 0
        return maxsum
            
        