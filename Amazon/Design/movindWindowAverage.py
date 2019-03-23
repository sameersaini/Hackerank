"""
The idea is to use deque to keep track of the nums as deque allows popLeft in nearly O(1)
and the use a separate variable to keep track of the sum.
"""

from collections import deque


class MovingAverage(object):

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.arr = deque()
        self.sum = 0
        self.size = size

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        if len(self.arr) == 0:
            self.arr.append(val)
            self.sum = val

            return val / 1

        if len(self.arr) >= self.size:
            poped = self.arr.popleft()
            self.arr.append(val)

            self.sum = self.sum - poped + val
            return self.sum / self.size
        else:
            self.arr.append(val)

            self.sum += val
            return self.sum / len(self.arr)

        # Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)