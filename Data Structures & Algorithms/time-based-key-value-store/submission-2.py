class TimeMap:

    def __init__(self):
        self.cache = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.cache[key].append((timestamp,value))

        

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        for value in self.cache[key]:
            if value[0]<=timestamp:
                res = value[1]
            else:
                break
        return res


        
