def safe(row, col, grid, visited):
    return row >= 0 and row < len(grid) and col >= 0 and col < len(grid[0]) and not visited[row][col] and grid[row][
        col] == 1


def DFS(row, col, grid, visited):
    visited[row][col] = True
    rows = [-1, 1, 0, 0]
    cols = [0, 0, -1, 1]

    for i in range(4):
        if safe(row + rows[i], col + cols[i], grid, visited):
            DFS(row + rows[i], col + cols[i], grid, visited)


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        grid = [[int(col) for col in row] for row in grid]
        visited = [[False for col in range(len(row))] for row in grid]

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if not visited[i][j] and grid[i][j] == 1:
                    islands += 1
                    DFS(i, j, grid, visited)

        return islands
