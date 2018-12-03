class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {}
        i = 0

        while i < len(nums):
            if nums[i] in d:
                nums.pop(i)
            else:
                d[nums[i]] = 1
                i += 1

        return len(nums)