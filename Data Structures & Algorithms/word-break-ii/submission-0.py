class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordset = set(wordDict)
        n = len(s)
        dp = [[] for _ in range(n+1)]
        dp[0] = [""]
        for i in range(1,n+1):
            for j in range(i):
                if s[j:i] in wordset:
                    for sentense in dp[j]:
                        dp[i].append((sentense+" "+ s[j:i]).strip())
        return dp[n]
        