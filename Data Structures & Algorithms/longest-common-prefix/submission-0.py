class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = strs[0]
        for s in strs[1:]:
            new_res = ""
            for i,c in enumerate(s):
                if i<len(res):
                    if s[i]==res[i]:
                        new_res+=s[i]
                    else:
                        break
            res = new_res
        return res
        