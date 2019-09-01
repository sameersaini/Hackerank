class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        neighbors = 0
        islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    islands += 1
                    if i < len(grid) - 1 and grid[i + 1][j] == 1: neighbors += 1
                    if j < len(grid[0]) - 1 and grid[i][j + 1] == 1: neighbors += 1

        return islands * 4 - neighbors * 2
