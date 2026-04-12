class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj={i:[] for i in range(n)}
        for n1,n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        visit=set()
        def dfs(i):
            if i in visit:
                return False
            visit.add(i)
            for j in adj[i]:
                dfs(j)
            return True
        count = 0
        for i in range(n):
            print(visit)
            if dfs(i):count+=1
        return count
        