
import math
class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Its a fibonacci series in O(1)
        n = n + 1

        rootFive = 5 ** 0.5

        phi = (1 + rootFive) / 2
        negativePhi = (1 - rootFive) / 2

        ans = (phi**n - (negativePhi)**n) / rootFive

        return int(ans)
