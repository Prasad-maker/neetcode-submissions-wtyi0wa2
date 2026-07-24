class Solution:
    def totalNQueens(self, n: int) -> int:
        col = set()
        pdiag = set()
        ndiag = set()
        res = 0
        def backtrack(r):
            nonlocal res
            if r==n:
                res+=1
                return
            for c in range(n):
                if c in col or (r+c) in pdiag or (r-c) in ndiag:
                    continue
                col.add(c)
                pdiag.add(r+c)
                ndiag.add(r-c)
                backtrack(r+1)
                col.remove(c)
                pdiag.remove(r+c)
                ndiag.remove(r-c)
        backtrack(0)
        return res


        