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
            times.append([False,interval.end])
            times.append([True,interval.start])
        count = 0
        days = 0
        times.sort(key=lambda x:(x[1],x[0]))
        for time in times:
            if time[0]:
                count+=1
                days=max(days,count)
            else:
                count-=1
        return days

            

        