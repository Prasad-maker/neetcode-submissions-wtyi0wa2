class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        points = []
        for passengers, start,end in trips:
            points.append([start,passengers])
            points.append([end,-passengers])
        points.sort()
        cursum = 0
        for point,passengers in points:
            cursum+=passengers
            if cursum > capacity:
                return False
        return True

        