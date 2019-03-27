"""
A simple O(M + N) solution is to have 2 arrays of size M and N and use these arrays to keep track of
which row and column should me marked with zeros.
A better solution is to use the first row and first column of the original matrix to keep track
of which row and which col should be marked as zero.
Also, keep two flags, one for first row and one for first col to track if first row and first col
should be marked with zeros or not.
"""

class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        if len(matrix) == 0:
            return matrix

        isFirstRowZero = False
        isFirstColZero = False

        for row in range(len(matrix)):
            if matrix[row][0] == 0:
                isFirstColZero = True
                break

        for col in range(len(matrix[0])):
            if matrix[0][col] == 0:
                isFirstRowZero = True
                break

        for row in range(1, len(matrix)):
            for col in range(1, len(matrix[0])):
                if matrix[row][col] == 0:
                    matrix[row][0] = 0
                    matrix[0][col] = 0

        for row in range(1, len(matrix)):
            for col in range(1, len(matrix[0])):
                if matrix[row][0] == 0 or matrix[0][col] == 0:
                    matrix[row][col] = 0

        if isFirstColZero:
            for row in range(len(matrix)):
                matrix[row][0] = 0

        if isFirstRowZero:
            for col in range(len(matrix[0])):
                matrix[0][col] = 0

