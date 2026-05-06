class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = {i:[] for i in range(n)}
        for node1,node2 in edges:
            adj[node1].append(node2)
            adj[node2].append(node1)
        visit = set()
        def dfs(node,par):
            if node in visit:
                return False
            visit.add(node)
            for nei in adj[node]:
                if nei==par:
                    continue
                if not dfs(nei,node):
                    return False
            return True
        return dfs(0,-1) and len(visit)==n