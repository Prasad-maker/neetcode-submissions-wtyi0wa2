class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n,m = len(s),len(t)
        dp = [0]*(m+1)
        dp[m]=1
        nextdp = [0]*(m+1)
        nextdp[m] = 1
        for i in range(n-1,-1,-1):
            for j in range(m-1,-1,-1):
                nextdp[j]=dp[j]
                if s[i]==t[j]:
                    nextdp[j]+=dp[j+1]
            dp = nextdp[:]
        return dp[0]



