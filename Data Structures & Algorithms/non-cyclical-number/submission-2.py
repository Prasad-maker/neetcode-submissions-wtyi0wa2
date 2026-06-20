class Solution:
    def isHappy(self, n: int) -> bool:
        fast,slow = self.sumofdigitsquares(n),n
        power = lam = 1

        while fast!=slow:
            if power ==lam:
                slow = fast
                power*=2
                lam=0
            fast = self.sumofdigitsquares(fast)
            if fast==1:
                return True
            lam+=1
        return False if fast!=1 else True
    
    def sumofdigitsquares(self,n):
        res = 0
        while n :
            digit = n%10
            res+=digit**2
            n//=10
        return res
        