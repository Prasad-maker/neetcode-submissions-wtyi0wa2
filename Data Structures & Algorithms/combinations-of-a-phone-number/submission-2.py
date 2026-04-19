class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        cur = []
        numtochr = {
            2: "abc",
            3: "def",
            4: "ghi",
            5: "jkl",
            6: "mno",
            7: "pqrs",
            8: "tuv",
            9: "wxyz",
        }

        def dfs(n):
            if n >= len(digits):
                res.append("".join(cur))
                return
            for c in numtochr[int(digits[n])]:
                cur.append(c)
                dfs(n + 1)
                cur.pop()
        if digits:
            dfs(0)
        return res
