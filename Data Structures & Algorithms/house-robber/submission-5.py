class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1,rob2 = 0,0
        for i in range(len(nums)):
            temp=rob1
            rob1 = max(rob2+nums[i],rob1)
            rob2=temp
        return rob1



        