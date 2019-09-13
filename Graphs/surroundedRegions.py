class Solution:
    def safe(self, board, row, col, visited):
        return row >= 0 and row < len(board) and col >= 0 and col < len(board[0]) and not visited[row][col] and \
               board[row][col] == 'O'

    def dfs(self, board, row, col, req, replace):
        rows = [0, 0, -1, 1]
        cols = [-1, 1, 0, 0]
        maxRow = len(board)
        maxCol = len(board[0])

        if row < 0 or row >= maxRow or col < 0 or col >= maxCol:
            return

        if board[row][col] != req:
            return

        board[row][col] = replace

        for i in range(4):
            self.dfs(board, row + rows[i], col + cols[i], "-", "O")

    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if len(board) == 0:
            return board

        rows = len(board)
        cols = len(board[0])

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "O":
                    board[i][j] = "-"

        # first row
        for i in range(cols):
            if board[0][i] == '-':
                self.dfs(board, 0, i, "-", "O")

        # first col
        for i in range(rows):
            if board[i][0] == '-':
                self.dfs(board, i, 0, "-", "O")

        # last row
        for i in range(cols):
            if board[rows - 1][i] == '-':
                self.dfs(board, rows - 1, i, "-", "O")

        # last col
        for i in range(rows):
            if board[i][cols - 1] == '-':
                self.dfs(board, i, cols - 1, "-", "O")

        for i in range(1, len(board) - 1):
            for j in range(1, len(board[0]) - 1):
                if board[i][j] == "-":
                    board[i][j] = "X"
