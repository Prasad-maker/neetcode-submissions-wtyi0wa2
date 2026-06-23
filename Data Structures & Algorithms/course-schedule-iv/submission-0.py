class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = defaultdict(list)
        for u,v in prerequisites:
            adj[v].append(u)
        prereqmap = {}
        def dfs(crs):
            if crs not in prereqmap:
                prereqmap[crs] = set()
                for prereq in adj[crs]:
                    prereqmap[crs] |= dfs(prereq)
                prereqmap[crs].add(crs)
            return prereqmap[crs]
        for crs in range(numCourses):
            dfs(crs)
        res = []
        for u,v in queries:
            res.append(u in prereqmap[v])
        return res
        
            
        