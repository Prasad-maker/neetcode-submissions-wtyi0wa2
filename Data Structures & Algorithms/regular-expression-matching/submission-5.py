class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m,n = len(s),len(p)
        dp = [False]*(n+1)
        dp[n] = True
        
        for i in range(m,-1,-1):
            nextdp = [False]*(n+1)
            nextdp[n]=(i==len(s))
            for j in range(n-1,-1,-1):
                match = i<len(s) and( s[i]==p[j] or p[j]==".")
                if (j+1)<len(p) and p[j+1]=="*":
                    nextdp[j] = nextdp[j+2]
                    if match:
                        nextdp[j] = dp[j] or nextdp[j]
                elif match:
                    nextdp[j] = dp[j+1]
            dp = nextdp[:]
        return nextdp[0]
                        