"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        times = []
        for interval in intervals:
            times.append([interval.start,1])
            times.append([interval.end,-1])
        count = 0
        days = 0
        times.sort(key=lambda x:(x[0],x[1]))
        for time in times:
            count+=time[1]
            days=max(days,count)
        return days

            

        