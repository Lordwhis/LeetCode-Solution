import heapq

class Twitter:

    def __init__(self):
        self.tweets = {}      # userId -> list of (time, tweetId)
        self.following = {}   # userId -> set of followeeIds
        self.time = 0

    def postTweet(self, userId, tweetId):
        if userId not in self.tweets:
            self.tweets[userId] = []

        self.tweets[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId):
        # User's own tweets + tweets from people they follow
        users = self.following.get(userId, set()).copy()
        users.add(userId)

        heap = []

        # Add the most recent tweet from each user
        for user in users:
            if user in self.tweets and self.tweets[user]:
                index = len(self.tweets[user]) - 1
                time, tweetId = self.tweets[user][index]

                heapq.heappush(heap, (-time, tweetId, user, index))

        result = []

        while heap and len(result) < 10:
            _, tweetId, user, index = heapq.heappop(heap)
            result.append(tweetId)

            # Add the next older tweet from the same user
            index -= 1

            if index >= 0:
                time, tweetId = self.tweets[user][index]
                heapq.heappush(
                    heap,
                    (-time, tweetId, user, index)
                )

        return result

    def follow(self, followerId, followeeId):
        if followerId not in self.following:
            self.following[followerId] = set()

        self.following[followerId].add(followeeId)

    def unfollow(self, followerId, followeeId):
        if followerId in self.following:
            self.following[followerId].discard(followeeId)
