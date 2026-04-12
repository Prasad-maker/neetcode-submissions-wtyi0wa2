class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = defaultdict(list)
        for s in strs:
            arr = [0]*26
            for c in s:
                arr[ord(c)-ord('a')]+=1
            arr=tuple(arr)
            hmap[arr].append(s)
        res = []
        for v in hmap.values():
            res.append(v)
        return res
            

        