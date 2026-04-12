class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def dfs(cur,i, total):
            if total == target:
                res.append(cur.copy())
                return
            for j in range(i,len(candidates)):
                if j>i and candidates[j] == candidates[j-1]:
                    continue
                if candidates[j]+total>target:
                    break
                cur.append(candidates[j])
                dfs(cur,j+1,total+candidates[j])
                cur.pop()
        dfs([],0,0)
        return res
        