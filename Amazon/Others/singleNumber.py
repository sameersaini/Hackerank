"""
The idea is to XOR the entire array and utilize the XOR property x ^ x == 0 and x ^ x ^ y = y
So as we are sure that one one number is occuring whereas others are occuring twice, so we can use the properties of the XOR
to obtain the ans
"""

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        single = nums[0]

        for num in nums[1:]:
            single ^= num

        return single
