class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res=[]
        board = [["."]*n for i in range(n)]
        cols = set()
        rows = set()
        pdiag = set() #r+c
        ndiag = set() #r-c

        def dfs(r):
            if r==n:
                board_cp = board.copy()
                res.append(["".join(row) for row in board_cp])
                return
            for c in range(n):
                if r in rows or c in cols or r+c in pdiag or r-c in ndiag:
                    continue
                cols.add(c)
                rows.add(r)
                pdiag.add(r+c)
                ndiag.add(r-c)
                board[r][c]="Q"
                dfs(r+1)
                cols.remove(c)
                rows.remove(r)
                pdiag.remove(r+c)
                ndiag.remove(r-c)
                board[r][c]="."
        dfs(0)
        return res

            
        