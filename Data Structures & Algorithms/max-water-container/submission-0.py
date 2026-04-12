class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l=0
        r=len(heights)-1
        mw = 0
        while(l<r):
            mw=max(mw,(r-l)*min(heights[l],heights[r]))
            if heights[l]>heights[r]:
                r-=1
            else:
                l+=1
        return mw


        