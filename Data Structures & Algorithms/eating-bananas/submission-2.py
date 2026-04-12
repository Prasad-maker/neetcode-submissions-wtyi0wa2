class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        res = float("inf")
        l,r = 1, max(piles)
        def isvalid(k):
            t=0
            for n in piles:
                t+= math.ceil(n/k)
            return t<=h
        while l<=r:
            
            m=(l+r)//2
            print(m)
            if isvalid(m):
                res = min(res,m)
                r=m-1
            else:
                l=m+1
        return res
       


        