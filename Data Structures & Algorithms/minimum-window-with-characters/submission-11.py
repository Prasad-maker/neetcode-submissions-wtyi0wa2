class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t: return ""
        tmap ={}
        for c in t:
            tmap[c] = tmap.get(c,0)+1
        have,need = 0, len(tmap)
        l = 0
        res,reslen = s, float("inf")
        wmap = {}
        for r in range(len(s)):
            wmap[s[r]] = wmap.get(s[r],0)+1
            if s[r] in tmap and tmap[s[r]] == wmap[s[r]]:
                have+=1
            while have==need:
                if reslen>=(r-l+1):
                    print(r,l)
                    res = s[l:r+1]
                    reslen=r-l+1
                wmap[s[l]] -=1
                if s[l] in tmap and tmap[s[l]]>wmap[s[l]]:
                    have -=1
                l+=1
        return res if  reslen!=float("inf") else ""

            
            

        
            
            

            


        