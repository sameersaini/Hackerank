class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m == 1 or n == 1:
            return 1

        grid = [[0 for _ in range(n)] for _ in range(m)]

        # mark first row 1
        for i in range(n):
            grid[0][i] = 1

        # mark first col 1
        for i in range(m):
            grid[i][0] = 1

        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] = grid[i][j - 1] + grid[i - 1][j]

        return grid[m - 1][n - 1]
