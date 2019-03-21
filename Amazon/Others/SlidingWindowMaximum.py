"""
The idea is to use deque of the size of k and for every num in the array nums, we only keep
numbers greater than that number in the deque.
Then, for all indexes greater than k-1, we pick the first element of the array as a maximum for
that window.
deque is used coz it performs pop, append, popleft, appendLeft in nearly o(1)
"""

from collections import deque


class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if len(nums) == 0:
            return []
        if k == 1:
            return nums

        queue = deque()
        ans = []

        for i in range(len(nums)):
            last = len(queue) - 1
            while last >= 0 and nums[queue[last]] < nums[i]:
                queue.pop()
                last -= 1
            if len(queue) > 0:
                first = queue[0]
                if (i - first) >= k:
                    queue.popleft()
            queue.append(i)
            if i >= k - 1:
                ans.append(nums[queue[0]])
        return ans
