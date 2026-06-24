class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t:
            return ""
        map_t = defaultdict(int)
        for c in t:
            map_t[c] += 1
        need = len(map_t)
        have = 0

        map_s = defaultdict(int)
        res,reslen = [-1,-1],float("inf")
        r,l = 1,0
        for r in range(len(s)):
            c = s[r]
            map_s[c]+=1
            if c in map_t:
                if map_t[c] == map_s[c]:
                    have+=1
            while have==need:
                if r-l+1<reslen:
                    res = [l,r]
                    reslen = r-l+1
                map_s[s[l]]-=1
                if s[l] in map_t and map_s[s[l]]<map_t[s[l]]:
                    have-=1
                l+=1
        return s[res[0]:res[1]+1] if reslen!= float("inf") else ""
                    


        