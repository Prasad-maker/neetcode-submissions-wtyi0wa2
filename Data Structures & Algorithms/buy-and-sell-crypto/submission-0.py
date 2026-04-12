class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        nmin = prices[0]
        profit = 0
        for i in range(1,len(prices)):
            profit=max(profit,prices[i]-nmin)
            nmin = min(nmin,prices[i])
        return profit
        