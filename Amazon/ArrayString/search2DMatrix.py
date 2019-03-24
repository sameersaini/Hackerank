"""
The idea is to do a Binary search in the N x M matrix.
start = 0
end = N x M - 1
mid = (start + end) // 2

The row and col for middle element are obtained as:
row = mid / M
col = mid % M

The perform the regular binary search to find the target

"""
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False

        start = 0
        end = len(matrix) * len(matrix[0]) - 1

        while start <= end:
            mid = (start + end) // 2

            row = mid // len(matrix[0])
            col = mid % len(matrix[0])

            if target == matrix[row][col]:
                return True
            elif target > matrix[row][col]:
                start = mid + 1
            else:
                end = mid - 1

        return False
