class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        visited = set()
        cycle = set()
        res = []
        adj = {i:[] for i in range(numCourses)}
        for cou,dep in prerequisites:
            adj[cou].append(dep)
        def dfs(course):
            if course in cycle:
                return False
            if course in visited:
                return True
            cycle.add(course)
            for dep in adj[course]:
                if not dfs(dep):
                    return False
            visited.add(course)
            cycle.remove(course)
            res.append(course)
            return True
        for i in range(numCourses):
            if not dfs(i):
                return []
        return res
        