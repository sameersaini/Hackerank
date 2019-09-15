class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]

        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if (mid == 0 and nums[mid] != nums[mid + 1]) or (mid == len(nums) - 1 and nums[mid] != nums[mid - 1]) or (
                    nums[mid] != nums[mid - 1] and nums[mid] != nums[mid + 1]):
                return nums[mid]

            if nums[mid] == nums[mid - 1]:
                if mid % 2 == 1:
                    left = mid + 1
                else:
                    right = mid - 1

            if nums[mid] == nums[mid + 1]:
                if mid % 2 == 0:
                    left = mid + 1
                else:
                    right = mid - 1