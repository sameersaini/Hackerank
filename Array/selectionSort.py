class Solution(object):
    def selectionSort(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(len(nums)):
            minIndex = i
            for j in range(i, len(nums)):
                if nums[j] < nums[minIndex]:
                    minIndex = j

            nums[i], nums[minIndex] = nums[minIndex], nums[i]

        return nums
