class Twitter:

    def __init__(self):
        self.count = 0
        self.following = defaultdict(set)
        self.tweets = defaultdict(list)
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append([self.count,tweetId])
        self.count -= 1

        

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minheap = []
        self.following[userId].add(userId)
        for followeeid in self.following[userId]:
            if followeeid in self.tweets:
                index = len(self.tweets[followeeid])-1
                count, tweetid = self.tweets[followeeid][index]
                heapq.heappush(minheap, [count,tweetid,followeeid,index-1])
        while minheap and len(res)<10:
            count,tweetid,followeeid,index = heapq.heappop(minheap)
            res.append(tweetid)
            if index>=0:
                count, tweetid = self.tweets[followeeid][index]
                heapq.heappush(minheap, [count,tweetid,followeeid,index-1])
        return res

        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)
        
