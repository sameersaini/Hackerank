class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if len(s) == 0 or numRows == 1:
            return s

        ans = [[] for _ in range(numRows)]

        forwardDirection = True

        row = 0

        for char in s:
            ans[row].append(char)

            if forwardDirection:
                row += 1
            else:
                row -= 1

            if row >= numRows:
                row -= 2
                forwardDirection = False
            if row == -1:
                row += 2
                forwardDirection = True

        returnString = ""
        for row in ans:
            for char in row:
                returnString += char

        return returnString
