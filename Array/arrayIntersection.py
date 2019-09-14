class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if len(nums1) < len(nums2):
            nums1, nums2 = nums2, nums1

        valuMap = {}

        for num in nums1:
            valuMap[num] = 1

        ans = []

        for num in nums2:
            if num in valuMap:
                del valuMap[num]
                ans.append(num)

        return ans
