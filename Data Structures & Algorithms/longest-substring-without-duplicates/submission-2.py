class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        l=0
        r=1
        maxl = 1
        while(r<len(s)):
            if s[r] not in s[l:r]:
                r+=1
                maxl=max(r-l,maxl)
            else:
                l+=1
        return maxl

        