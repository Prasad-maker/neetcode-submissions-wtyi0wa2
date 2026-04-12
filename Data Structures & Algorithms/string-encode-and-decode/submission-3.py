class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res+=str(len(s))+"#"+s
        return res

    def decode(self, s: str) -> List[str]:
        num = ""
        res = []
        i=0
        while i<len(s):
            if s[i]!="#":
                num+=s[i]
            else:
                num = int(num)
                res.append(s[i+1:i+1+num])
                i+=num
                num =""
            i+=1
        return res
            

            



