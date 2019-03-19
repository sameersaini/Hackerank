"""
This is similar to fibonacci sequence
"""
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1 or n == 2:
            return n

        a = 1
        b = 2

        for _ in range(n - 2):
            total = a + b
            a = b
            b = total

        return total
