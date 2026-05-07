class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = [False]*n
        res =0
        adj = {i:[] for i in range(n)}
        for n1,n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        def dfs(node):
            for nei in adj[node]:
                if not visited[nei]:
                    visited[nei]=True
                    dfs(nei)
        for i in range(n):
            if not visited[i]:
                visited[i]=True
                dfs(i)
                res+=1
        return res
        