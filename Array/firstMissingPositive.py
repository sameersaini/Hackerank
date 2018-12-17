def swapNumbers(arr):
    j = 0
    for i in range(len(arr)):
        if arr[i] <= 0:
            arr[i], arr[j] = arr[j], arr[i]
            j += 1

    return j

class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        shift = swapNumbers(nums)
        nums = nums[shift:]

        for i in range(len(nums)):
            num = abs(nums[i])
            if  num-1 < len(nums) and nums[num-1] > 0:
                nums[num-1] = -nums[num-1]

        i = 0
        while i < len(nums):
            if nums[i] > 0:
                break
            i += 1

        return i+1
