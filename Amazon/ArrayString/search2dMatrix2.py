class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) == 0:
            return False

        row = 0
        col = len(matrix[0]) - 1

        while col >= 0 and row < len(matrix):
            current = matrix[row][col]
            if target == current:
                return True
            elif target < current:
                col -= 1
            else:
                row += 1

        return False
