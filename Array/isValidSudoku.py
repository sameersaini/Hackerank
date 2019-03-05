class Solution:
    # checks condition 1
    def checkRows(self, board):
        for row in board:
            values = {}
            for char in row:
                if char != '.' and char in values:
                    return False
                else:
                    values[char] = 1
        return True

    # checks condition 2
    def checkCols(self, board):
        for col in range(9):
            values = {}
            for row in range(9):
                if board[row][col] != '.' and board[row][col] in values:
                    return False
                else:
                    values[board[row][col]] = 1
        return True

    # checks condition 3
    def checkSubGrid(self, board):
        for row in range(3):
            startRow = row * 3
            endRow = startRow + 3
            for col in range(3):
                startCol = col * 3
                endCol = startCol + 3
                values = {}
                for i in range(startRow, endRow):
                    for j in range(startCol, endCol):
                        if board[i][j] != '.' and board[i][j] in values:
                            return False
                        else:
                            values[board[i][j]] = 1
        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return self.checkRows(board) and self.checkCols(board) and self.checkSubGrid(board)
