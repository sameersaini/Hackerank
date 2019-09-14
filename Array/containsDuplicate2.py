class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        hashMap = {}

        for i in range(len(nums)):
            if nums[i] in hashMap:
                return True

            hashMap[nums[i]] = 1

            if i >= k:
                del hashMap[nums[i - k]]

        return False
