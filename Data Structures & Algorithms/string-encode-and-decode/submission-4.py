class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s))+"#"+s
        return res

    def decode(self, s: str) -> List[str]:
        temp = ""
        res = []
        i = 0
        while i<len(s):
            if s[i]=="#":
                l = int(temp)
                word = s[i+1:i+1+l]
                res.append(word)
                temp = ""
                i+=1+l
            else:
                temp += s[i]
                i+=1
        return res
            
