class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        hmap={}
        res = []
        for i in range(len(s)):
            hmap[s[i]]=i
        end = 0
        size=0 
        for i in range(len(s)):
            end=max(end,hmap[s[i]])
            size+=1
            if i==end:
                res.append(size)
                size = 0
        return res
            
            