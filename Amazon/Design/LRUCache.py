"""
The idea is to use 2 DS: deque and a hashmap/dictionary
"""

from collections import deque


class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.queue = deque()
        self.items = {}

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.items:
            self.queue.remove(key)
            self.queue.appendleft(key)
            return self.items[key]
        else:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.items:
            self.queue.remove(key)
        else:
            if len(self.queue) == self.capacity:
                del self.items[self.queue[-1]]
                self.queue.pop()

        self.queue.appendleft(key)
        self.items[key] = value

    # Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)