class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS,COLS = len(heights), len(heights[0])
        pac, atl = set(), set()
        visited = set()

        def dfs(r,c,preVal):
            if ((r,c) in visited or r<0 or r>=ROWS or c<0 or c>=COLS or heights[r][c]<preVal):
                return
            visited.add((r,c))
            dfs(r-1,c,heights[r][c])
            dfs(r+1,c,heights[r][c])
            dfs(r,c-1,heights[r][c])
            dfs(r,c+1,heights[r][c])
        for c in range(COLS):
            visited = pac
            dfs(0,c,heights[0][c])
            visited = atl
            dfs(ROWS-1,c,heights[ROWS-1][c])
        for r in range(ROWS):
            visited = pac
            dfs(r,0,heights[r][0])
            visited = atl
            dfs(r,COLS-1,heights[r][COLS-1])
        res=[]
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in pac and (r,c) in atl:
                    res.append([r,c])
        return res


            

            
        