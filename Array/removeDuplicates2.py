class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        startIndex = 0
        counter = 0
        i = 0
        while i < len(nums):
            temp = nums[i]

            while i < len(nums) and nums[i] == temp:
                i += 1
                counter += 1

            if counter > 2: counter = 2

            for _ in range(counter):
                nums[startIndex] = temp
                startIndex += 1

            counter = 0

        return startIndex
