class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp,value))
        

    def get(self, key: str, timestamp: int) -> str:
        l=0
        r=len(self.store[key])-1
        val=""
        while(l<=r):
            m=(l+r)//2
            if self.store[key][m][0]<=timestamp:
                val=self.store[key][m][1]
                l=m+1
            else:
                r=m-1
        return val

        
