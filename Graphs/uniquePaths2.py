class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])
        dpGrid = [[0 for _ in range(len(obstacleGrid[0]))] for _ in range(len(obstacleGrid))]

        # mark first row 1
        for i in range(len(obstacleGrid[0])):
            if obstacleGrid[0][i] == 1:
                break
            dpGrid[0][i] = 1

        # mark first col 1
        for i in range(len(obstacleGrid)):
            if obstacleGrid[i][0] == 1:
                break
            dpGrid[i][0] = 1

        for i in range(1, len(obstacleGrid)):
            for j in range(1, len(obstacleGrid[0])):
                if obstacleGrid[i][j] == 1:
                    continue
                dpGrid[i][j] = dpGrid[i][j - 1] + dpGrid[i - 1][j]

        return dpGrid[rows - 1][cols - 1]