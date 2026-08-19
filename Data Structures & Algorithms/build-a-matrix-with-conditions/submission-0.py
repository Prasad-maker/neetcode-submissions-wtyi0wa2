class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        res = [[0]*k for _ in range(k)]
        def dfs(src,adj,visit,path,order):
            if src in path:
                return False
            if src in visit:
                return True
            visit.add(src)
            path.add(src)
            for nei in adj[src]:
                if not dfs(nei,adj,visit,path,order):
                    return False
            path.remove(src)
            order.append(src)
            return True
        def topo_order(edges):
            adj = defaultdict(list)
            for u,v in edges:
                adj[u].append(v)
            visit,path  = set(),set()
            order = []
            for src in range(1,k+1):
                if not dfs(src,adj,visit,path,order):
                    return []
            return order[::-1]


        row_order = topo_order(rowConditions)
        col_order = topo_order(colConditions)
        if not row_order or not col_order:
            return []
        val_to_row = {n:i for i,n in enumerate(row_order)}
        val_to_col = {n:i for i,n in enumerate(col_order)}
        for i in range(1,k+1):
            r,c = val_to_row[i],val_to_col[i]
            res[r][c] = i
        return res
        