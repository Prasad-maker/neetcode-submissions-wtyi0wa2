class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):return False
        a1 = [0]*26
        a2 = [0]*26
        for c in s1:
            a1[ord(c)-ord('a')] +=1
        for c in s2[:len(s1)]:
            a2[ord(c)-ord('a')] +=1
        if a1==a2:return True
        for l in range(len(s2)-len(s1)):
            a2[ord(s2[l])-ord('a')]-=1
            a2[ord(s2[l+len(s1)])-ord('a')]+=1
            if a1==a2:return True
        return False





        
        