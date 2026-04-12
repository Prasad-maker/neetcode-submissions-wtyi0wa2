class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        let = {"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        cur = []
        def dfs(i):
            if i==len(digits):
                if cur:
                    res.append("".join(cur))
                return
            for l in let[digits[i]]:
                cur.append(l)
                dfs(i+1)
                cur.pop()
        dfs(0)
        return res

        