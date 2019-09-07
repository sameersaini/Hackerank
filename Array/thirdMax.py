class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        nums = list(set(nums))
        first, second, third = nums[0], nums[0], nums[0]

        for num in nums:
            if num >= first:
                third = second
                second = first
                first = num
            elif num >= second:
                third = second
                second = num
            elif num >= third:
                third = num

        if len(nums) >= 3:
            return third
        else:
            return first