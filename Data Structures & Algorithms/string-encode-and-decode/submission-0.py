class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for st in strs:
            res+=str(len(st))+"#"+st
        return res


    def decode(self, s: str) -> List[str]:
        ln = ""
        c=0
        words = []
        while c<len(s):
            if s[c]!="#":
                ln+=s[c]
            else:
                words.append(s[c+1:c+1+int(ln)])
                c+=int(ln)
                ln=""
            c+=1
        return words



