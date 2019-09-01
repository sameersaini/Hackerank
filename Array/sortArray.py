class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) == 0:
            return nums

        bucket = {}
        for i in range(-50000, 50000 + 1):
            bucket[i] = 0

        for num in nums:
            bucket[num] += 1

        ans = []
        for i in range(-50000, 50000 + 1):
            if bucket[i] != 0:
                for _ in range(bucket[i]): ans.append(i)

        return ans
