class Solution(object):
    def safe(self, grid, visited, currentRow, currentCol):
        return currentRow >= 0 and currentRow < len(grid) and currentCol >= 0 and currentCol < len(grid[0]) and \
               grid[currentRow][currentCol] == 1 and not visited[currentRow][currentCol]

    def bfs(self, grid, visited, queue):
        area = 1
        rows = [-1, 1, 0, 0]
        cols = [0, 0, -1, 1]

        while len(queue) > 0:
            row, col = queue.pop(0)

            for i in range(4):
                currentRow = row + rows[i]
                currentCol = col + cols[i]
                if self.safe(grid, visited, currentRow, currentCol):
                    area += 1
                    visited[currentRow][currentCol] = True
                    queue.append([currentRow, currentCol])

        return area

    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if len(grid) == 0:
            return 0

        maxArea = 0

        visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and not visited[i][j]:
                    queue = [[i, j]]
                    visited[i][j] = True
                    area = self.bfs(grid, visited, queue)
                    maxArea = max(area, maxArea)

        return maxArea
