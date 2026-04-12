class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = defaultdict(list)
        for w in strs:
            wl = [0]*26
            for c in w:
                wl[ord(c)-ord('a')] +=1
            wl = tuple(wl)
            hmap[wl].append(w)
        res = []
        for v in hmap.values():
            res.append(v)
        return res


        