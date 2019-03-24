"""
Sieve of Eratosthenes solution
"""

class Solution:
    def countPrimes(self, n: int) -> int:
        arr = [True for _ in range(n)]
        ret = 0
        for i in range(2, int(n ** 0.5) + 1):
            if arr[i]:
                for j in range(2 * i, n, i):
                    arr[j] = False

        for i in range(2, n):
            if arr[i]:
                ret += 1

        return ret