class Solution:
    def checkValidString(self, s: str) -> bool:
        leftmin,leftmax = 0,0
        for c in s:
            if c=="(":
                leftmax+=1
                leftmin+=1
            elif c==")":
                leftmax-=1
                leftmin-=1
            else:
                leftmax+=1
                leftmin-=1
            if leftmax<0:
                return False
            if leftmin<0:
                leftmin=0
        return leftmin==0
        