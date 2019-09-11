class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        if len(grid) == 0:
            return 0

        dpArr = [[-1 for _ in range(len(grid[0]))] for _ in range(len(grid))]

        dpArr[0][0] = grid[0][0]

        # fill the first row
        for i in range(1, len(grid[0])):
            dpArr[0][i] = dpArr[0][i - 1] + grid[0][i]

        # fill the first column
        for i in range(1, len(grid)):
            dpArr[i][0] = dpArr[i - 1][0] + grid[i][0]

        for i in range(1, len(grid)):
            for j in range(1, len(grid[0])):
                dpArr[i][j] = grid[i][j] + min(dpArr[i][j - 1], dpArr[i - 1][j])

        return dpArr[len(grid) - 1][len(grid[0]) - 1]
