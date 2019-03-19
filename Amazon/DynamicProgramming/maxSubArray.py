"""
The idea is to use kadane's algorithm in which for every index we find the max sum till that index
and then for the next index the the maxSum is
the max of value at that index or maxSum till previous index + value at that index
"""
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        maxSum = currentMax = nums[0]
        for num in nums[1:]:
            currentMax = max([num, currentMax + num])
            if currentMax > maxSum:
                maxSum = currentMax
        return maxSum
