class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        minprice = prices[0]
        for price in prices[1:]:
            res = max(price-minprice,res)
            minprice = min(minprice,price)
        return res
        
        