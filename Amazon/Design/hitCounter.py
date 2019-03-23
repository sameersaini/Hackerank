"""
A brute force approach can be to use a array and record every timestamp
and then while getting check each timestamp to count hits in last 5 mins

A better approach has been implemented here and is given as:

Maintain two counters of size 300:
hits to record the hits
timestamps to record the latest timestamps

For hit:
    we store the latest timestamp in the timestamps array for any timestamp in range 0 to 299
    For this do timestamp % 300 to find the index to store the value.
    If current timestamp at that index is different then we update the index with new timestamp
    and set the index in hit array to 1
    Else: we increment the hit array at index by 1

For Get:
    For every index we check if the timestamp at that index is within the 300 sec
    If yes, then we pick the count from hits array

    Finally, we return the final count
"""

class HitCounter(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hits = [0 for _ in range(300)]
        self.timestamps = [0 for _ in range(300)]

    def hit(self, timestamp):
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: None
        """
        index = timestamp % 300
        if self.timestamps[index] != timestamp:
            self.timestamps[index] = timestamp
            self.hits[index] = 1
        else:
            self.hits[index] += 1

    def getHits(self, timestamp):
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: int
        """
        ans = 0
        for i in range(300):
            if timestamp - self.timestamps[i] < 300:
                ans += self.hits[i]

        return ans

# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)