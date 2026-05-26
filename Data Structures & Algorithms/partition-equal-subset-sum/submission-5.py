class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        n = len(nums)
        if total%2:
            return False
        target = total//2
        dp = [False]*(target+1)
        dp[0] = True
        for i in range(n):
            for j in range(target,nums[i]-1,-1):
                dp[j] = dp[j] or dp[j-nums[i]]
        return dp[-1]
