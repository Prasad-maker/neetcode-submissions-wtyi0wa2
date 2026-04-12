class TimeMap:

    def __init__(self):
        self.db = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.db[key].append((timestamp,value))
        

    def get(self, key: str, timestamp: int) -> str:
        value = ""
        l,r = 0, len(self.db[key])-1
        while r>=l:
            m= (l+r)//2
            if self.db[key][m][0]>timestamp:
                r=m-1
            else:
                value=self.db[key][m][1]
                l+=1
        return value

        
