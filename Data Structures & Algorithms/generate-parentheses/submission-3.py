class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        cur = []
        def dfs(openN,closedN):
            if openN == closedN ==n:
                res.append("".join(cur))
                return
            if openN<n:
                cur.append("(")
                dfs(openN+1,closedN)
                cur.pop()
            if closedN<openN:
                cur.append(")")
                dfs(openN,closedN+1)
                cur.pop()
        dfs(0,0)
        return res

        