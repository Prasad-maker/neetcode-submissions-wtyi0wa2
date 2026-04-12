class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=1
        res=[1]*len(nums)
        for i in range(len(nums)-1):
            n*=nums[i]
            res[i+1]*=n
        n=1
        for i in range(len(nums)-1,0,-1):
            n*=nums[i]
            res[i-1]*=n
        return res