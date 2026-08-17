"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':

        def dfs(n,r,c):
            val = grid[r][c]
            node = Node(val,True)
            allsame = True
            for i in range(n):
                for j in range(n):
                    if grid[r+i][c+j]!=val:
                        allsame=False
                        break
            if allsame:
                return node
            node.topLeft = dfs(n//2,r,c)
            node.topRight = dfs(n//2,r,c+n//2)
            node.bottomLeft = dfs(n//2,r+n//2,c)
            node.bottomRight = dfs(n//2,r+n//2,c+n//2)
            node.val = 0
            node.isLeaf = False
            return node
        return dfs(len(grid),0,0)
        