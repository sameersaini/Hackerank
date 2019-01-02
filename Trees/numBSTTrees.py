from math import factorial
class Solution:
    def numTrees(self, n):
        """
        Catalan Number Cn
        """
        ans = factorial(2*n)/(factorial(n+1)*factorial(n))

        return int(ans)
