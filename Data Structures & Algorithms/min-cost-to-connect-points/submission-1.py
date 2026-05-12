class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n= len(points)
        visit = [False]*n
        dist = [float("inf")]*n
        node = 0
        res = 0
        edges=0
        while edges<n-1:
            visit[node]=True
            nextnode = -1
            for i in range(n):
                if visit[i]:
                    continue
                curdist = (abs(points[i][0]-points[node][0])+abs(points[i][1]-points[node][1]))
                dist[i]=min(dist[i],curdist)
                if nextnode==-1 or dist[i]<dist[nextnode]:
                    nextnode = i
            res +=dist[nextnode]
            node=nextnode
            edges+=1
        return res
                
        