class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res,cur = [],[]
        n=len(s)
        dp = [[False]*(n) for i in range(n)]
        for end in range(n):
            for start in range(end,-1,-1):
                if s[start]==s[end] and (end-start<=2 or dp[start+1][end-1]):
                    dp[start][end] = True
        print(dp)
        def subpali(i):
            if i>=n:
                res.append(cur.copy())
                return 
            for j in range(i,n):
                if dp[i][j]:
                    cur.append(s[i:j+1])
                    subpali(j+1)
                    cur.pop()
        subpali(0)
        return res
    
        