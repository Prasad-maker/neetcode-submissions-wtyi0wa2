class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        temp = nums.copy()
        def dfs(idx,temp):
            if idx==len(temp):
                res.append(temp.copy())
                return
            for i in range(idx,len(temp)):
                temp[idx],temp[i] = temp[i],temp[idx]
                dfs(idx+1,temp)
                temp[i],temp[idx] = temp[idx],temp[i]
        dfs(0,temp)
        return res
        