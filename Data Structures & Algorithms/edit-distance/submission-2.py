class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m,n = len(word1),len(word2)
        if m>n:
            n,m=m,n
            word1,word2 = word2,word1
        dp = [float("inf")]*(n+1) 
        nextdp = [float("inf")]*(n+1) 
        for i in range(n+1):
            dp[i] = n-i
        
        for i in range(m-1,-1,-1):
            nextdp[n] = m-i
            for j in range(n-1,-1,-1):
                if word1[i]==word2[j]:
                    nextdp[j]=dp[j+1]
                else:
                    nextdp[j] = 1+min(dp[j],dp[j+1],nextdp[j+1])
            dp = nextdp[:]
        return dp[0]
        
        