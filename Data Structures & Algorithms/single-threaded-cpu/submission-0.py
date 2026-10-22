class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        n = len(tasks)
        indices = list(range(n))
        indices.sort(key=lambda i:(tasks[i][0],i))
        class Task:
            def __init__(self,idx) :
                self.idx = idx
            def __lt__(self,other):
                if tasks[self.idx][1] != tasks[other.idx][1]:
                    return tasks[self.idx][1] < tasks[other.idx][1]
                return self.idx <other.idx
        minheap = []
        res = []
        time = i= 0
        while minheap or i<n:
            while i<n and tasks[indices[i]][0]<=time:
                heapq.heappush(minheap,Task(indices[i]))
                i+=1
            if not minheap :
                time = tasks[indices[i]][0]
            else:
                next_task = heapq.heappop(minheap)
                time += tasks[next_task.idx][1]
                res.append(next_task.idx)
        return res

        