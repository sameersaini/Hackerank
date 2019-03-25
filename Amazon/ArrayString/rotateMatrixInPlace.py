"""
The Idea is to transpose the matrix first
Then, reverse each row for clockwise rotation
      reverse each col for anticlockwise rotation
"""

class Solution:
    def printMatrix(self, matrix):
        for row in matrix:
            print(row)

    def transpose(self, matrix):
        for row in range(len(matrix)):
            for col in range(row, len(matrix[0])):
                matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]

    def rotateClockwise(self, matrix):
        for row in range(len(matrix)):
            for col in range(len(matrix) // 2):
                matrix[row][col], matrix[row][-1 - col] = matrix[row][-1 - col], matrix[row][col]

    def rotateAntiClockwise(self, matrix):
        for col in range(len(matrix)):
            for row in range(len(matrix) // 2):
                matrix[row][col], matrix[-1 - row][col] = matrix[-1 - row][col], matrix[row][col]

    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return matrix

        # transpose the matrix
        self.transpose(matrix)

        # reverse each row for clockwise and reverse each column for anticlockwise
        self.rotateClockwise(matrix)
