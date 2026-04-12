class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q=collections.deque()
        fresh = 0
        time = 0
        dirs = [[-1,-0],[0,-1],[0,1],[1,0]]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    fresh+=1
                elif grid[i][j]==2:
                    q.append((i,j))
        while(q and fresh):
            for i  in range(len(q)):
                f=q.popleft()
                for dirc in dirs:
                    x=f[0]+dirc[0]
                    y=f[1]+dirc[1]
                    if ( x in range(len(grid)) and y in range(len(grid[0])) and grid[x][y] ==1 ):
                        grid[x][y]=2
                        q.append((x,y))
                        fresh-=1
            time+=1
        return time if fresh==0 else -1
                    

                
