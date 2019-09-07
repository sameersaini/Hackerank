class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        if len(nums) == 0:
            return False

        currentIndex = len(nums) - 1
        index = len(nums) - 1

        while index >= 0:
            if index + nums[index] >= currentIndex:
                currentIndex = index
            index -= 1

        return currentIndex == 0
