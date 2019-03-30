"""
This is a recursive solution where we maintain 2 pointers open and close to maintain the count
of open and close parens.

if close == n(total pair of parens) then we append the string to the array and return
if open < n then we append ( to string and call the function with open + 1
if open > close, then we append ) to string and call the function with close + 1
"""
class Solution:
    def generateParens(self, s, n, open, close, arr):
        if close == n:
            arr.append(s)
            return
        else:
            if open < n:
                temp = s
                temp += "("
                self.generateParens(temp, n, open + 1, close, arr)

            if open > close:
                temp = s
                temp += ")"
                self.generateParens(temp, n, open, close + 1, arr)

    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return []
        arr = []
        self.generateParens("", n, 0, 0, arr)

        return arr
