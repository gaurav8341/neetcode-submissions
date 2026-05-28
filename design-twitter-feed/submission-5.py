from collections import defaultdict
import heapq

class Twitter:

    def __init__(self):
        # we should have a dict holding tweets of every user.
        # need another dict with set of all the followee of the user.
        self.posts = defaultdict(list)
        self.followees = defaultdict(set)
        self.count = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        # Tweet is posted
        self.posts[userId].append([self.count, tweetId])
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        feed = [] 
        # also include his own tweets.
        feed.extend(self.posts[userId])
        for f in self.followees[userId]:
            if f == userId:
                continue
            feed.extend(self.posts[f])
        heapq.heapify(feed)

        result_feed = []
        while len(result_feed) < 10 and feed:
            post = heapq.heappop(feed)
            result_feed.append(post[1])
        
        return result_feed

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followees[followerId].add(followeeId)
        print(self.followees)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        followees = self.followees[followerId]
        if followeeId in followees:
            followees.remove(followeeId)
        print(self.followees)


