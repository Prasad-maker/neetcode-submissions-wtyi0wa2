class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        n= len(nums)
        dp =[[float("inf")]*(k+1) for _ in range(n+1)]
        dp[n][0] = 0
        for i in range(n-1,-1,-1):
            for m in range(1,k+1):
                cursum = 0
                for j in range(i,n-m+1):
                    cursum+=nums[j]
                    dp[i][m] = min(dp[i][m],max(cursum,dp[j+1][m-1]))
        return dp[0][k]


        