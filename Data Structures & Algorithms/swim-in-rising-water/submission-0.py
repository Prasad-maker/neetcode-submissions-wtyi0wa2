class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N=len(grid)
        visit =  set()
        minheap = [[grid[0][0],0,0]]
        visit.add((0,0))
        dirs = [[0,1],[0,-1],[1,0],[-1,0]]
        while minheap:
            t,r,c = heapq.heappop(minheap)
            if r==N-1 and c==N-1:
                return t
            for dr,dc in dirs:
                neir,neic = r+dr,c+dc
                if (neir<0 or neic<0 or neir==N or neic==N or (neir,neic) in visit):
                    continue
                visit.add((neir,neic))
                heapq.heappush(minheap,[max(t,grid[neir][neic]),neir,neic])
        