class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        visited =set()
        maxarea = 0
        ROWS,COLS=len(grid),len(grid[0])
        def dfs(r,c):
            if r<0 or c<0 or r==ROWS or c==COLS or grid[r][c]==0 or (r,c) in visited:
                return 0
            visited.add((r,c))
            area =1
            area +=dfs(r+1,c)
            area +=dfs(r-1,c)
            area +=dfs(r,c+1)
            area +=dfs(r,c-1)
            return area
        for r in range(ROWS):
            for c in range(COLS):
                maxarea=max(dfs(r,c),maxarea)
        return maxarea
        