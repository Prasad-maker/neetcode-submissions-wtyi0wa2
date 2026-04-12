class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1: return nums[0]
        return max(self.helper(nums[1::]),self.helper(nums[:-1]))
    def helper(self,ns):
        rob1,rob2 = 0,0
        for n in ns:
            temp = rob1
            rob1 = max(rob2+n,rob1)
            rob2=temp
        return rob1


        