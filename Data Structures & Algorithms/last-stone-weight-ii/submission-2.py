class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        n = len(stones)
        stonesum = sum(stones)
        target = stonesum//2
        dp = [0]*(target+1) 
        for i in range(1,n+1):
            for t in range(target,-1,-1):
                if t>= stones[i-1]:
                    dp[t] = max(dp[t],dp[t-stones[i-1]]+stones[i-1])
        return stonesum - 2* dp[target]

        