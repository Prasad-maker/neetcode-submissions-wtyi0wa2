class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        max_val = max(interval[0] for interval in intervals)
        mp = [0]*(max_val+1)
        for start,end in intervals:
            mp[start] = max(end+1,mp[start])
        res = []
        have = -1
        intervals_start = -1
        for i in range(len(mp)):
            if mp[i] != 0:
                if intervals_start==-1:
                    intervals_start =i
                have = max(mp[i]-1, have)
            if have == i:
                res.append([intervals_start,have])
                have = -1
                intervals_start = -1

        if intervals_start!= -1:
            res.append([intervals_start,have])
        return res


        