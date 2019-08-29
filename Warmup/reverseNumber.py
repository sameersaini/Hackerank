class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        isNegative = False
        if x < 0:
            isNegative = True
            x = -x

        reverse = 0

        while x > 0:
            remainder = x % 10
            x = x // 10

            reverse = reverse * 10 + remainder

        if isNegative:
            reverse = -reverse

        if reverse < -2 ** 31 or reverse > 2 ** 31 - 1:
            return 0

        return reverse