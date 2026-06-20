class Solution:
    def isHappy(self, n: int) -> bool:
        fast,slow = self.sumofdigitsquares(n),n
        print(self.sumofdigitsquares(100))
        while fast!=slow:
            slow = self.sumofdigitsquares(slow)
            fast = self.sumofdigitsquares(self.sumofdigitsquares(fast))
            if fast==1 or slow==1:
                return True
        return False if fast!=1 else True
    
    def sumofdigitsquares(self,n):
        res = 0
        while n :
            digit = n%10
            res+=digit**2
            n//=10
        return res
        