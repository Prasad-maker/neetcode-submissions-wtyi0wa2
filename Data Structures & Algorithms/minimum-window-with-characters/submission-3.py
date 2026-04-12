class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t=="": return ""
        tmap = {}
        for c in t:
            tmap[c]=1+tmap.get(c,0)
        res=[-1,-1]
        reslen=float("infinity")
        smap ={}
        have,need = 0,len(tmap)
        l=0
        for i in range(len(s)):
            smap[s[i]]=1+smap.get(s[i],0)
            if s[i] in tmap and smap[s[i]] ==tmap.get(s[i]):
                have+=1
            while(need==have ):
                if (i-l+1)<reslen:
                    res = [l,i]
                    reslen = i-l+1
                print(smap)
                smap[s[l]]-=1
                if s[l] in t and smap[s[l]] < tmap.get(s[l],0):
                    have-=1
                l+=1
        l,r =res
        return s[l:r+1] if reslen!=float("infinity") else""
            
            

            


        