class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        ar = [0]*(len(cost)+1)
        for i in range(2,len(cost)+1):
            ar[i] = min(ar[i-1]+cost[i-1],ar[i-2]+cost[i-2])
        return ar[-1]
        