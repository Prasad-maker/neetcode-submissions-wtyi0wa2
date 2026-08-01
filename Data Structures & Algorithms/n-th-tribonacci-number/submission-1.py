class Solution:
    def tribonacci(self, n: int) -> int:
        t0,t1,t2 = 0,1,1
        if n<3:
            if n ==0:
                return 0
            else:
                return 1
        for i in range(n-2):
            t3 = t0 + t1 + t2
            t0,t1,t2 = t1,t2,t3
        return t3
        