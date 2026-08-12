class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        n= len(nums)
        dp =[float("inf")]*(n+1)
        dp[n] = 0
        for m in range(1,k+1):
            new_dp = [float("inf")]*(n+1)
            for i in range(n-1,-1,-1):
                
                cursum = 0
                for j in range(i,n-m+1):
                    cursum+=nums[j]
                    new_dp[i] = min(new_dp[i],max(cursum,dp[j+1]))
            dp = new_dp.copy()
        return dp[0]


        