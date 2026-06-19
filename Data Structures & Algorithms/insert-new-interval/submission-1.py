class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        newIntervaladded = False
        for i,[l,r] in enumerate(intervals):
            if r < newInterval[0]:
                res.append([l,r])
            elif l>newInterval[1]:
                res.append(newInterval)
                return res+intervals[i:]
            else:
                newInterval = [min(l,newInterval[0]),max(newInterval[1],r)]
        res.append(newInterval)

        return res