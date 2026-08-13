class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        res = 0
        dp = [0] *(target+1)
        dp[0]=1
        for i in range(target):
            for num in nums:
                if num+i>target:
                    continue
                dp[num+i]+=dp[i]


        return dp[-1]