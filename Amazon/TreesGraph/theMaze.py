"""
The idea is to do a BFS from the starting position.
This is different from normal BFS as we one we move in a direction we keep on moving until
we hit a boundary.
When we hit a boundary then we check if the previous position has already been visited or not.
If not visited, then we mark it visited and add it to the queue.

When we pop from the queue, then we check whether the popped node is the destination or not.

The main idea is to keep only those destinations in the queue which are hard stop boundaries.
If any hard stop boundary is the destination, then we return True else we return False in the end.
"""

class Solution:
    def safe(self, maze, currX, currY):
        return currX >= 0 and currX < len(maze) and currY >= 0 and currY < len(maze[0]) and maze[currX][currY] == 0

    def bfs(self, maze, visited, start, destination):
        rows = [0, 0, 1, -1]
        cols = [-1, 1, 0, 0]
        queue = [start]
        visited[start[0]][start[1]] = True

        while len(queue) > 0:
            poped = queue.pop(0)
            x, y = poped[0], poped[1]

            if x == destination[0] and y == destination[1]:
                return True

            for i in range(4):
                currX = x + rows[i]
                currY = y + cols[i]

                while self.safe(maze, currX, currY):
                    currX += rows[i]
                    currY += cols[i]

                if not visited[currX - rows[i]][currY - cols[i]]:
                    visited[currX - rows[i]][currY - cols[i]] = True
                    queue.append([currX - rows[i], currY - cols[i]])

        return False

    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        visited = [[False for _ in range(len(maze[0]))] for _ in range(len(maze))]

        return self.bfs(maze, visited, start, destination)