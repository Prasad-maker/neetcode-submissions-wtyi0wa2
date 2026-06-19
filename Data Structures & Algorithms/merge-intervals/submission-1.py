class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:(x[0],x[1]))
        L,R = intervals[0]
        res = []
        for l,r in intervals[1:]:
            if l>R:
                res.append([L,R])
                L,R = l,r
            else:
                L=min(L,l)
                R=max(R,r)
        res.append([L,R])
        return res


        