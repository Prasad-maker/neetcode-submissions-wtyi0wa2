class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        cur = []
        def dfs(n):
            if n==len(nums):
                res.append(cur.copy())
                return
            cur.append(nums[n])
            dfs(n+1)
            cur.pop()
            i = n+1
            while i<len(nums) and nums[i]==nums[n]:
                i+=1
            dfs(i)
        dfs(0)
        return res
        