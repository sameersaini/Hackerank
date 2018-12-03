class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        left = 0
        right = len(nums) - 1

        while left < right:
            mid = left + (right - left)//2

            if nums[mid] == target:
                return mid

            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        if target <= nums[left]:
            return left
        else:
            return left + 1