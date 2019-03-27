"""
Well for n bits, there can be 2 power n numbers. 2 power n can be given by 1 << n
For every number i from 0 to 1 << n: gray code can be obtained i ^ i >> 1
i.e. i xor [i/2] i xor with i right shift 1. right shift i by 1 essentially divides i by 2.

For example:
    for n = 2
    numbers can be 0,1,2,3 and for every number gray code can be obtained as i ^ i >> 1

    0 -> 0000 -> 0 ^ 0 >> 1 -> 0000 ^ 0000 = 0000 -> 0
    1 -> 0001 -> 1 ^ 1 >> 1 -> 0001 ^ 0000 = 0001 -> 1
    2 -> 0010 -> 2 ^ 2 >> 1 -> 0010 ^ 0001 = 0011 -> 3
    3 -> 0011 -> 3 ^ 3 >> 1 -> 0011 ^ 0001 = 0010 -> 2

    So for n = 2, gray code is [0, 1, 3, 2]
"""
class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        ans = []
        for i in range(1 << n):
            ans.append(i ^ i >> 1)

        return ans
