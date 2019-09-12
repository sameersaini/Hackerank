class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        current_max = nums[0]
        current_min = nums[0]
        prev_max = nums[0]
        prev_min = nums[0]
        ans = nums[0]

        for num in nums[1:]:
            current_max = max(prev_max * num, prev_min * num, num)
            current_min = min(prev_max * num, prev_min * num, num)
            ans = max(ans, current_max)
            prev_max = current_max
            prev_min = current_min

        return ans
