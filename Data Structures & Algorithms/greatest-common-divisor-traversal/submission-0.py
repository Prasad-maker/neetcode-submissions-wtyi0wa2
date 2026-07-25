class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        n = len(nums)
        if n==1:
            return True
        if any(num==1 for num in nums):
            return False
        MAX = max(nums)
        sieve = [0]*(MAX+1)
        p=2
        while p*p <=MAX:
            if sieve[p] == 0:
                for composite in range(p*p, MAX+1,p):
                    sieve[composite] = p
            p+=1
        visit = set()
        adj = defaultdict(list)
        for i in range(n):
            num = nums[i]
            if sieve[num] == 0:
                adj[i].append(n+num)
                adj[n+num].append(i)
                continue
            while num>1:
                prime = sieve[num] if sieve[num]!=0 else num
                adj[i].append(n+prime)
                adj[n+prime].append(i)
                while num%prime==0:
                    num//=prime
        def dfs(node):
            visit.add(node)
            for nei in adj[node]:
                if nei not in visit:
                    dfs(nei)
        dfs(0)
        for i in range(n):
            if i not in  visit:
                return False
        return True

        