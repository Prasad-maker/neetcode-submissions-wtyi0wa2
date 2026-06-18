class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxindex = 0
        for i in range(len(nums)-1):
            maxindex = max(maxindex,i+nums[i])
            if i>=maxindex:
                return False
            
        return True

        