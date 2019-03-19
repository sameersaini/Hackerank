"""
The idea is to implement a variation of quicksort called quickselect
The algo sorts in ascending order so to pick the Kth largest element, change k to len(nums) - k
If the position(Index) returned by the partition is equal to the K, the return the element at the Index
The the Index is larger than K, the sort in left subarray, else sort the right subarray.

If we pick the rightmost element as pivot, then in worstcase this algo will also run in O(N^2)
So, we use the randomPivot fn to randomly pick the pivot, which increase the efficiency of the algo
"""


import random


class Solution(object):
    def quicksort(self, nums, left, right, k):
        index = self.partition(nums, left, right)
        if index - left == k:
            return nums[index]

        if index - left > k:
            return self.quicksort(nums, left, index - 1, k)
        else:
            return self.quicksort(nums, index + 1, right, k - index + left - 1)

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
        return self.quicksort(nums, 0, len(nums) - 1, len(nums) - k)
