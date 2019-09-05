class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        start = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[start] = nums[i]
                start += 1

        for i in range(start, len(nums)):
            nums[i] = 0
