class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        max_so_far = nums[0]
        max_ending = nums[0]

        for num in nums[1:]:
            max_ending = max(num, max_ending+num)

            if max_ending > max_so_far:
                max_so_far = max_ending


        return max_so_far