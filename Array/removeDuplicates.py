class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        i = 1
        start = 1

        while i < len(nums):
            while i < len(nums) and nums[i] == nums[i - 1]:
                i += 1

            if i < len(nums):
                nums[start] = nums[i]
                start += 1
                i += 1

        return start
