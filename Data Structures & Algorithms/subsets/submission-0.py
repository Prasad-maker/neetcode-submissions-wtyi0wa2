class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        def dfs(i):
            if i>=len(nums):
                res.append(subset.copy())
                return
            subset.append(nums[i])
            dfs(i+1)
            del subset[-1]
            dfs(i+1)
            return
        dfs(0)
        return res
        