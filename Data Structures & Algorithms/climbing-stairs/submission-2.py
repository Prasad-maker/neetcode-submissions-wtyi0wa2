class Solution:
    def climbStairs(self, n: int) -> int:
        ar = [0]*(n+1)
        ar[0],ar[1]=1,1
        for i in range(2,n+1):
            ar[i]=ar[i-1]+ar[i-2]
        return ar[-1] 


        