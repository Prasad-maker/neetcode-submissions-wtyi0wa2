class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        adj1 = defaultdict(set)
        adj2 = defaultdict(set)
        res = []
        for a,b in trust:
            adj1[b].add(a)
            adj2[a].add(b)

        for s in adj1:
            if len(adj1[s])== n-1 and len(adj2[s])==0:
                res.append(s)
        return res[0] if len(res)==1 else -1

        