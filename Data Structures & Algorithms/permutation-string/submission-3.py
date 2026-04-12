class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        arr1 = [0]*26
        for c in s1:
            arr1[ord(c)-ord('a')] +=1
        arr2 = [0]*26
        for c in s2[:len(s1)]:
            arr2[ord(c)-ord('a')] +=1
        l=0
        r=len(s1)
        if arr1==arr2: return True
        while r<len(s2):
            arr2[ord(s2[r])-ord('a')] +=1
            arr2[ord(s2[l])-ord('a')] -=1
            if arr1==arr2: return True
            r+=1
            l+=1
        return False



        