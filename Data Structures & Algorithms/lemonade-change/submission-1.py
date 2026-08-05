class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        a = b =  0
        for bill in bills:
            if bill == 5:
                a+=1
            if bill == 10:
                if a<1:
                    return False
                a-=1
                b+=1
            if bill == 20:
                if a<1:
                    return False
                if b<1:
                    if a<3:
                        return False
                    a-=3
                else:
                    b-=1
                    a-=1
        return True
        