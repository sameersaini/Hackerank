class TicTacToe:

    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        self.size = n
        self.grid = [['' for _ in range(n)] for _ in range(n)]
        self.maxMoves = n * n
        self.currentMoves = 0
        self.moves = {
            1: 'X',
            2: 'O'
        }

    def printGrid(self):
        for row in self.grid:
            print(row)

    def checkWin(self, move, row, col):
        # checking col wise
        for i in range(self.size):
            if self.grid[row][i] != move:
                break
        else:
            return True

        # checking col wise
        for i in range(self.size):
            if self.grid[i][col] != move:
                break
        else:
            return True

        # checking down diagonal wise
        for i in range(self.size):
            if self.grid[i][i] != move:
                break
        else:
            return True

        # checking up diagonal wise
        for i in range(self.size):
            if self.grid[i][self.size - i - 1] != move:
                break
        else:
            return True

        return False

    def move(self, row: int, col: int, player: int) -> int:
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """
        if self.grid[row][col] == '':
            move = self.moves[player]
            self.grid[row][col] = move
            self.currentMoves += 1

            if self.checkWin(move, row, col):
                if move == self.moves[1]:
                    return 1
                else:
                    return 2

        # self.printGrid()
        # print()
        if self.currentMoves <= self.maxMoves:
            return 0

        # Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)