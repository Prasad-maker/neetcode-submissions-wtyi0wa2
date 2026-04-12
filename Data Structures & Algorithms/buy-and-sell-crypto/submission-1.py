class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        nmin = prices[0]
        max_p = 0
        for i in prices:
            max_p = max(max_p,i-nmin)
            nmin = min(nmin,i)
        return max_p
            

        