class Solution(object):
    def matchWord(self, board, row, col, word, level):
        if level == len(word):
            return True

        if row < 0 or col < 0 or row >= len(board) or col >= len(board[0]):
            return False

        if board[row][col] == word[level]:
            temp = board[row][col]
            board[row][col] = '#'
            ret = self.matchWord(board, row - 1, col, word, level + 1) or self.matchWord(board, row + 1, col, word,
                                                                                         level + 1) or self.matchWord(
                board, row, col - 1, word, level + 1) or self.matchWord(board, row, col + 1, word, level + 1)
            board[row][col] = temp
            return ret

        return False

    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if len(board) == 0:
            return False

        rows = len(board)
        cols = len(board[0])

        if rows * cols < len(word):
            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if self.matchWord(board, i, j, word, 0):
                        return True

        return False
