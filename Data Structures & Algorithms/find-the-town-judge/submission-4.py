class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        delta = defaultdict(int)
        res = -1
        for a,b in trust:
            delta[b-1]+=1
            delta[a-1]-=1

        for s in range(n):
            if delta[s]==n-1:
                res= s
        return res+1 if res!=-1 else -1

        