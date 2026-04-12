class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = defaultdict(list)
        for s in strs:
            a = [0]*26
            for c in s:
                a[ord(c)-ord("a")]+=1
            hmap[tuple(a)].append(s)
        return hmap.values()

        