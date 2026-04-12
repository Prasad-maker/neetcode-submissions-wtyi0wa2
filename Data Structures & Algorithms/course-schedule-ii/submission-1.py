class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        premap = {i:[] for i in range(numCourses)}
        visit = set()
        for crs,pre in prerequisites:
            premap[crs].append(pre)
        output = []
        cycle = set()
        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visit:
                return True
            cycle.add(crs)
            for pre in premap[crs]:
                if not dfs(pre):
                    return False
            cycle.remove(crs)
            visit.add(crs)
            output.append(crs)
            return True
        for i in range(numCourses):
            if not dfs(i):return []

        return output

        