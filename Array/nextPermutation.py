"""
Algo:
    1. Find the index i from right such that nums[i] > nums[i-1]
        This means the all the numbers to the right of i-1 are already sorted in desc order.
    2. Find the index j for which the positive diff between i-1 and j is smallest.
    3. swap number at i-1 and j.
    4. reverse the numbers to the right of i-1.
"""

class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 0 or len(nums) == 1:
            return nums

        i = len(nums) - 1

        while i > 0 and nums[i] <= nums[i - 1]:
            i -= 1

        if i == 0 and nums[i] > nums[i + 1]:
            nums.sort()
            return

        location = i - 1

        minDiff = nums[i] - nums[i - 1]
        minDiffLocation = i
        for j in range(i, len(nums)):
            diff = nums[j] - nums[i - 1]
            if diff > 0 and diff <= minDiff:
                minDiff = diff
                minDiffLocation = j

        nums[location], nums[minDiffLocation] = nums[minDiffLocation], nums[location]

        left = location + 1
        right = len(nums) - 1

        while left < right:
            nums[left], nums[right] = nums[right], nums[left]

            left += 1
            right -= 1
