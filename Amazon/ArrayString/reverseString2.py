class Solution:
    def reverseStr(self, str, start, end):
        if start >= end:
            return
        str[start], str[end] = str[end], str[start]

        self.reverseStr(str, start + 1, end - 1)

    def reverseWords(self, str: List[str]) -> None:
        """
        Do not return anything, modify str in-place instead.
        """
        i = 0
        for j in range(len(str)):
            if str[j] == " ":
                self.reverseStr(str, i, j - 1)
                i = j + 1

        self.reverseStr(str, i, len(str) - 1)

        self.reverseStr(str, 0, len(str) - 1)