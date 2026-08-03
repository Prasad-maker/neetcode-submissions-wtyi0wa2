class Solution:
    def numSquares(self, n: int) -> int:
        dp = [n]*(n+1)
        dp[0]=0
        for i in range(n+1):
            for s in range(i+1):
                square = s*s
                if i-square<0:
                    break
                dp[i] = min(dp[i],dp[i-square]+1)
        return dp[n]

        