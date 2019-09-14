class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        i = 1

        while i <= n:
            if i == n:
                return True

            i = i << 1

        return False
