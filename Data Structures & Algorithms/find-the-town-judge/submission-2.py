class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        incoming = [0]*n
        outgoing = [0]*n
        res = -1
        for a,b in trust:
            incoming[b-1]+=1
            outgoing[a-1]+=1

        for s in range(n):
            if incoming[s]==n-1 and outgoing[s]==0:
                res= s
        return res+1 if res!=-1 else -1

        