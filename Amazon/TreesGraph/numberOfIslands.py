"""
The idea is to do a BFS of the grid to find the islands
Use a visited matrix to keep track of the indexes which has already been visited.
"""

class Solution(object):
    def safe(self, grid, i, j, visited):
        return i >= 0 and i < len(grid) and j >= 0 and j < len(grid[0]) and grid[i][j] == "1" and not visited[i][j]

    def bfs(self, grid, visited, queue):
        rows = [1, -1, 0, 0]
        cols = [0, 0, 1, -1]

        while len(queue) > 0:
            loc = queue.pop(0)
            i, j = loc[0], loc[1]
            visited[i][j] = True
            for k in range(4):
                temp_i = i + rows[k]
                temp_j = j + cols[k]
                if self.safe(grid, temp_i, temp_j, visited):
                    queue.append([temp_i, temp_j])
                    visited[temp_i][temp_j] = True

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        islands = 0
        if len(grid) == 0:
            return islands

        visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        islands = 0

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if not visited[i][j] and grid[i][j] == "1":
                    self.bfs(grid, visited, [[i, j]])
                    islands += 1

        return islands
