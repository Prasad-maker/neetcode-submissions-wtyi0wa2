class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def backtrack(i,path):
            if len(path)==k:
                res.append(list(path))
                return
            if i>n:
                return 
            for j in range(i,n+1):
                path.add(j)
                backtrack(j+1,path)
                path.remove(j)
        backtrack(1,set())
        return res

        