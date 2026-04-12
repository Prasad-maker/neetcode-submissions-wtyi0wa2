class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2==1:
            return False
        dp = set()
        dp.add(0)
        for i in range(len(nums)-1,-1,-1):
            newdp = set()
            for n in dp:
                newdp.add(nums[i]+n)
                newdp.add(n)
            dp=newdp
        if sum(nums)//2 in dp:
            return True
        return False
        