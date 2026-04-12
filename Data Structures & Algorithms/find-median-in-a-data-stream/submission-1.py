class MedianFinder:

    def __init__(self):
        self.smallheap = []
        self.bigheap = []
        

    def addNum(self, num: int) -> None:
        if self.bigheap and num> self.bigheap[0]:
            heapq.heappush(self.bigheap,num)
        else:
            heapq.heappush(self.smallheap,-num)
        if len(self.bigheap)-len(self.smallheap)>1:
            heapq.heappush(self.smallheap,-heapq.heappop(self.bigheap))
        elif len(self.smallheap)-len(self.bigheap)>1:
            heapq.heappush(self.bigheap,-heapq.heappop(self.smallheap))


        

    def findMedian(self) -> float:
        if len(self.bigheap)>len(self.smallheap):
            return self.bigheap[0]
        elif len(self.bigheap)<len(self.smallheap):
            return -self.smallheap[0]
        else:
            return (-self.smallheap[0]+self.bigheap[0])/2
        
        