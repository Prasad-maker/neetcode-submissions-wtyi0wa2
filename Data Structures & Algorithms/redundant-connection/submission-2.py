class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        cycle = set()
        visit = set()
        cyclestart = -1
        def dfs(node,par):
            nonlocal cyclestart
            if node in visit:
                cyclestart = node
                return True
            visit.add(node)
            for nei in adj[node]:
                if nei==par:
                    continue
                if dfs(nei,node):
                    if cyclestart!=-1:
                        cycle.add(node)    
                    if node == cyclestart:
                        cyclestart=-1
                    return True
            return False
        dfs(1,-1)
        for u,v in reversed(edges):
            if u in cycle and v in cycle:
                return [u,v]
        return []