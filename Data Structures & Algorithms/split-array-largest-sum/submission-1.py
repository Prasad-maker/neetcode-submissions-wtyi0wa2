class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        n= len(nums)
        dp ={}
        def dfs(i,m):
            if (i,m) in dp:
                return dp[(i,m)]
            if i==n :
                return 0 if m== 0 else float("inf")
            if m==0:
                return float("inf")
            cursum = 0
            res = float("inf")
            for j in range(i,n-m+1):
                cursum+=nums[j]
                res = min(res,max(cursum,dfs(j+1,m-1)))
            dp[(i,m)] = res
            return res
        return dfs(0,k)


        