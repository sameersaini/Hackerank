class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if len(triangle) == 0:
            return 0

        dp = [num for num in triangle[-1]]
        i = len(triangle) - 2

        while i >= 0:
            arr = triangle[i]
            for j in range(len(arr)):
                dp[j] = min(dp[j], dp[j + 1]) + arr[j]

            i -= 1

        return dp[0]