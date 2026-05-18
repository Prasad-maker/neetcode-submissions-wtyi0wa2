class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1,rob2 = 0,0
        n=len(nums)
        for i in range(n):
            temp = rob1
            rob1=max(rob1,rob2+nums[i])
            rob2 = temp
        return rob1
        