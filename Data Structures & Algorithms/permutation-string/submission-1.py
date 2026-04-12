class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l=0
        map1 = [0]*26
        map2 = [0]*26
        if len(s1)>len(s2):
            return False
        for i in range(len(s1)):
            map1[ord(s1[i])-ord("a")]+=1
            map2[ord(s2[i])-ord("a")]+=1
        if map1==map2:
            return True
        for r in range(len(s1),len(s2)):
            map2[ord(s2[r])-ord('a')]+=1
            map2[ord(s2[r-len(s1)])-ord("a")]-=1
            if map1==map2:
                return True
        return False
            
            



        
        