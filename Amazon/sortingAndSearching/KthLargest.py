"""
The idea is to sort the array first and then pick the kth element from the end
I have used the quicksort to sort the array and in worst case it will run in O(N^2)
An efficient way is to do a quickselect variation of quicksort
"""

import random


class Solution(object):
    def quicksort(self, nums, left, right):
        if left >= right:
            return

        index = self.partition(nums, left, right)

        self.quicksort(nums, left, index - 1)
        self.quicksort(nums, index + 1, right)

    def partition(self, nums, left, right):
        self.randomPivot(nums, left, right)
        pivot = nums[right]

        i = left
        for j in range(left, right):
            if nums[j] < pivot:
                self.swap(nums, i, j)
                i += 1

        self.swap(nums, i, right)
        return i

    def randomPivot(self, nums, left, right):
        length = right - left
        pivot = random.randint(0, length)
        self.swap(nums, left + pivot, right)

    def swap(self, nums, left, right):
        nums[left], nums[right] = nums[right], nums[left]

    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        self.quicksort(nums, 0, len(nums) - 1)
        return nums[-k]
