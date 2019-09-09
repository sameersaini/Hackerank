class Solution(object):
    def heapPermutation(self, nums, size, ans):
        if size == 1:
            ans.append(nums[::])

        for i in range(size):
            self.heapPermutation(nums, size - 1, ans)

            if size % 2 == 1:
                nums[0], nums[size - 1] = nums[size - 1], nums[0]
            else:
                nums[i], nums[size - 1] = nums[size - 1], nums[i]

    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 0:
            return []

        ans = []

        self.heapPermutation(nums, len(nums), ans)

        return ans
