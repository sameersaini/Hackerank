class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if len(matrix) == 0:
            return []

        ans = []

        firstRow = 0
        firstCol = 0
        lastRow = len(matrix)
        lastCol = len(matrix[0])

        while firstRow < lastRow and firstCol < lastCol:
            for i in range(firstCol, lastCol):
                ans.append(matrix[firstRow][i])

            firstRow += 1

            for i in range(firstRow, lastRow):
                ans.append(matrix[i][lastCol - 1])

            lastCol -= 1

            if firstRow < lastRow:
                for i in range(lastCol - 1, firstCol - 1, -1):
                    ans.append(matrix[lastRow - 1][i])

                lastRow -= 1

            if firstCol < lastCol:
                for i in range(lastRow - 1, firstRow - 1, -1):
                    ans.append(matrix[i][firstCol])

                firstCol += 1

        return ans