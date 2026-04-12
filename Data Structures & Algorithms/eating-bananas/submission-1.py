class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        res= max(piles)
        l,r= 1,max(piles)
        while r>=l:
            t=0
            m=(r+l)//2
            for p in piles:
                t+=math.ceil(p/m)
            if t<=h:
                res = min(res,m)
                r=m-1
            else:
                l=m+1
        return res


        
        

        