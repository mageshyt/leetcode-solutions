'''Design a simplified version of Twitter where users can post tweets, follow/unfollow another user, and is able to see the 10 most recent tweets in the user's news feed.

Implement the Twitter class:

Twitter() Initializes your twitter object.
void postTweet(int userId, int tweetId) Composes a new tweet with ID tweetId by the user userId. Each call to this function will be made with a unique tweetId.
List<Integer> getNewsFeed(int userId) Retrieves the 10 most recent tweet IDs in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user themself. Tweets must be ordered from most recent to least recent.
void follow(int followerId, int followeeId) The user with ID followerId started following the user with ID followeeId.
void unfollow(int followerId, int followeeId) The user with ID followerId started unfollowing the user with ID followeeId.


Example 1:

Input
["Twitter", "postTweet", "getNewsFeed", "follow",
    "postTweet", "getNewsFeed", "unfollow", "getNewsFeed"]
[[], [1, 5], [1], [1, 2], [2, 6], [1], [1, 2], [1]]
Output
[null, null, [5], null, null, [6, 5], null, [5]]

Explanation
Twitter twitter = new Twitter();
twitter.postTweet(1, 5); // User 1 posts a new tweet (id = 5).
twitter.getNewsFeed(1);  // User 1's news feed should return a list with 1 tweet id -> [5]. return [5]
twitter.follow(1, 2);    // User 1 follows user 2.
twitter.postTweet(2, 6); // User 2 posts a new tweet (id = 6).
twitter.getNewsFeed(1);  // User 1's news feed should return a list with 2 tweet ids -> [6, 5]. Tweet id 6 should precede tweet id 5 because it is posted after tweet id 5.
twitter.unfollow(1, 2);  // User 1 unfollows user 2.
twitter.getNewsFeed(1);  // User 1's news feed should return a list with 1 tweet id -> [5], since user 1 is no longer following user 2.'''

import collections
import heapq


class Twitter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.posts = collections.defaultdict(
            list)  # {userId:[(tweetId)]} list going to be heap
        self.follows = collections.defaultdict(
            set)  # {userId:set(followeeId)} set to avoid duplicates

        self.timestamp = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        # compose a new tweet with ID tweetId by the user userId
        # we dont have max heap so we use negative tweetId to make it max heap
        # decrease timestamp by 1 to make sure the most recent tweet is at the top

        self.posts[userId].append((self.timestamp, tweetId))
        self.timestamp -= 1

    def getNewsFeed(self, userId: int):
        res = []  # list of tweetIds

        # get the 10 most recent tweet IDs from the user's own tweets and the tweets of the users they follow
        minHeap = []
        # user can follow himself
        self.follows[userId].add(userId)
        for followeeId in self.follows[userId]:
            if self.posts[followeeId]:
                idx = len(self.posts[followeeId])-1  # get the last tweet
                timestamp, tweetId = self.posts[followeeId][idx]
                heapq.heappush(
                    minHeap, (timestamp, tweetId, followeeId, idx-1))

        # get the 10 most recent tweet IDs
        while minHeap and len(res) < 10:
            timestamp, tweetId, followeeId, idx = heapq.heappop(minHeap)
            res.append(tweetId)
            if idx >= 0:
                timestamp, tweetId = self.posts[followeeId][idx]
                heapq.heappush(
                    minHeap, (timestamp, tweetId, followeeId, idx-1))
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        # the user with ID followerId started following the user with ID followeeId
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # the user with ID followerId started unfollowing the user with ID followeeId
        self.follows[followerId].discard(followeeId)


if __name__ == '__main__':
    twitter = Twitter()
    twitter.postTweet(1, 5)
    print(twitter.getNewsFeed(1))
    twitter.follow(1, 2)
    twitter.postTweet(2, 6)
    twitter.getNewsFeed(1)
    twitter.unfollow(1, 2)
    twitter.getNewsFeed(1)
