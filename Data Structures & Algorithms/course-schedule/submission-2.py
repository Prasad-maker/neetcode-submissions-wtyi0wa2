class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {i:[] for i in range(numCourses)}
        for cou,pre in prerequisites:
            adj[cou].append(pre)
        visiting =set()
        def dfs(crs):
            if crs in visiting:
                return False
            if adj[crs]==[]:
                return True
            visiting.add(crs)
            for dep in adj[crs]:
                if not dfs(dep):
                    return False
            visiting.remove(crs)
            adj[crs]=[]
            return True
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True

        
        