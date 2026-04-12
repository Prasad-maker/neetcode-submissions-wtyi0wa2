class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t: return ""
        have = 0
        hmap = {}
        hmap1 = {}
        res,reslen = [-1,-1],float("inf")
        l = 0
        for c in t:
            hmap[c]=1+hmap.get(c,0)
        need = len(hmap)
        for r in range(len(s)):
            hmap1[s[r]] = 1+hmap1.get(s[r],0)
            if s[r] in hmap and hmap[s[r]] == hmap1[s[r]]:
                have +=1
            while have==need:
                if (r-l+1)<reslen:
                    reslen = r-l+1
                    res = [l,r]
                hmap1[s[l]]-=1
                if s[l] in hmap and hmap[s[l]] > hmap1[s[l]]:
                    have-=1
                l+=1
        return s[res[0]:res[1]+1] if reslen!=float("inf")  else ""
            
            

        
            
            

            


        