class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        dp ={}
        dirs = [(-1,0),(1,0),(0,1),(0,-1)]
        ROWS,COLS = len(matrix),len(matrix[0])
        def dfs(sp,last_value):
            if sp[0]<0 or sp[0]>=ROWS or sp[1]<0 or sp[1]>=COLS or matrix[sp[0]][sp[1]]<=last_value:
                return 0
            if sp in dp:
                return dp[sp]
            length = 0
            for dr,dc in dirs:
                r,c = sp[0]+dr, sp[1]+dc
                length = max(length,dfs((r,c),matrix[sp[0]][sp[1]]))
            dp[sp] = 1+length
            return 1+length
        res = 0
        for i in range(ROWS):
            for j in range(COLS):
                res = max(res,dfs((i,j),-1))
        return res

            
        