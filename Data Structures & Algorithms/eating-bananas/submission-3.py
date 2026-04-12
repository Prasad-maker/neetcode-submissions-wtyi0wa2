class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        res = float("inf")
        l,r = 1, max(piles)
            
        while l<=r:
            m=(l+r)//2
            t=0
            for n in piles:
                t+= math.ceil(n/m)
            if  t<=h:
                res = min(res,m)
                r=m-1
            else:
                l=m+1
        return res
       


        