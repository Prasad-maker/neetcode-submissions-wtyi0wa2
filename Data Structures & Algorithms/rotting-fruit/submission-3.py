class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh_fruit = 0
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]==2:
                    q.append([r,c])
                elif grid[r][c]==1:
                    fresh_fruit+=1
        time=0
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        while q and fresh_fruit>0:
            length = len(q)
            for i in range(length):
                r,c = q.popleft()
                
                for dr,dc in directions:
                    row,col = r+dr, c+dc
                    if min(row,col)>=0 and row<ROWS and col<COLS and grid[row][col]==1:
                        grid[row][col]=2
                        q.append([row,col])
                        fresh_fruit-=1
            time+=1
        return time if fresh_fruit==0 else -1
                        


        