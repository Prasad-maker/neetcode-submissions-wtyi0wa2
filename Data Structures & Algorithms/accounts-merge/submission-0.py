class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        emailidx = {}
        emails = []
        emailtoacc = {}
        m= 0
        for accid,a in enumerate(accounts):
            for i in range(1,len(a)):
                email = a[i]
                if email in emailidx:
                    continue
                emails.append(email)
                emailidx[email] = m
                emailtoacc[m] = accid
                m+=1
        adj= [[] for _ in range(m)]
        for a in accounts:
            for i in range(2,len(a)):
                id1  = emailidx[a[i]]
                id2 = emailidx[a[i-1]]
                adj[id1].append(id2)
                adj[id2].append(id1)
        emailgroup = defaultdict(list)
        visited = [False]*m
        def dfs(node,accid):
            visited[node] = True
            emailgroup[accid].append(emails[node])
            for nei in adj[node]:
                if not visited[nei]:
                    dfs(nei,accid)
        for i in range(m):
            if not visited[i]:
                dfs(i,emailtoacc[i])


        res = []
        for accid in emailgroup:
            name = accounts[accid][0]
            res.append([name]+sorted(emailgroup[accid]))
        return res
        


        