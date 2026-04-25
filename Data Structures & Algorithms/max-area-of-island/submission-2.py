class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        res = 0
        ROWS,COLS = len(grid), len(grid[0])
        cur = 0
        def dfs(r,c):
            nonlocal res,cur
            if r<0 or c<0 or r>=ROWS or c>=COLS or grid[r][c]==0 or (r,c) in visited:
                res = max(res,cur)
                return 
            cur+=1
            visited.add((r,c))
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
        for r in range(ROWS):
            for c in range(COLS):
                cur=0
                dfs(r,c)
        return res
        