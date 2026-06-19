class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:[x[1],-x[0]])
        prevend = intervals[0][1]
        res=0
        for start,end in intervals[1:]:
            if start<prevend:
                res+=1
            else:
                prevend = end
        return res
        