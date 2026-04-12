class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {c:set() for word in  words for c in word  }
        for i in range(len(words)-1):
            w1,w2 = words[i],words[i+1]
            minlen = min(len(w1),len(w2))
            if w1[:minlen]==w2[:minlen] and len(w1)>len(w2):
                return ""
            for j in range(minlen):
                if w1[j] !=w2[j]:
                    adj[w1[j]].add(w2[j])
                    break
        visit = {}
        res = []
        def dfs(char):
            if char in visit:
                return visit[char]
            visit[char] = True
            for nei in adj[char]:
                if dfs(nei):
                    return True
            visit[char] = False
            res.append(char)
        for c in adj:
            if dfs(c):
                return ""
        res.reverse()
        return "".join(res)

