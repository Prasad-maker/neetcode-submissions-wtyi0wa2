class Solution:
    def numDecodings(self, s: str) -> int:
        one,two = 1,1
        for i in range(len(s)-1,-1,-1):
            temp=one
            if s[i]=="0":
                one=0
            if i+1<len(s) and (s[i]=="1" or (s[i]=="2" and s[i+1] in "0123456")):
                one+=two
            two=temp
        return one
            

                
        
            
        