class CountSquares:

    def __init__(self):
        self.pointscount = defaultdict(lambda: defaultdict(int))

    def add(self, point: List[int]) -> None:
        self.pointscount[point[0]][point[1]] +=1
        

    def count(self, point: List[int]) -> int:
        x1,y1 = point
        res = 0
        for y2 in self.pointscount[x1]:
            print(y2)
            side = y2-y1
            if side == 0:
                continue
            x3,x4 = x1+side,x1-side
            res += (self.pointscount[x1][y2]*self.pointscount[x3][y2] * self.pointscount[x3][y1])
            res += (self.pointscount[x1][y2]*self.pointscount[x4][y2] * self.pointscount[x4][y1])
        return res
        
