class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        res = ""
        count = [a,b,c]
        def getMax(repeated):
            idx = -1
            maxcnt = 0
            for i in range(3):
                if i==repeated or count[i]==0:
                    continue
                if maxcnt< count[i]:
                    maxcnt = count[i]
                    idx = i
            return idx
        repeated = -1
        while True:
            maxchar = getMax(repeated)
            if maxchar == -1:
                break
            char = chr(ord("a")+maxchar)
            count[maxchar]-=1
            if res and res[-1] == char:
                repeated = maxchar
            else:
                repeated=-1
            res+= char
        return res



        