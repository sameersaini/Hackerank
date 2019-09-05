class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        left = 0

        while left < len(nums):
            while left < len(nums) and nums[left] != 0:
                left += 1

            if left == len(nums):
                break

            temp = left + 1

            while temp < len(nums) and nums[temp] == 0:
                temp += 1

            if temp == len(nums):
                break

            nums[left], nums[temp] = nums[temp], nums[left]

        return left
