class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 5:
            return 0

        ans = 0
        i = 5

        while n // i > 0:
            ans += n // i
            i = i * 5

        return ans
