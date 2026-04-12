class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        hmap = {}
        res=0
        for r in range(len(s)):
            if s[r] in hmap:
                l = max(hmap[s[r]]+1,l)
            hmap[s[r]]=r
            res = max(res,r-l+1)
        return res

