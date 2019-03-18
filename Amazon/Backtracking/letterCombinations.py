class Solution(object):
    def dfs(self, numberCharMap, digits, words, current, index):
        if len(current) == len(digits):
            words.append(current)
            return

        for char in numberCharMap[digits[index]]:
            current += char
            self.dfs(numberCharMap, digits, words, current, index + 1)
            current = current[:-1]

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        numberCharMap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        words = []
        current = ""

        if len(digits) == 0:
            return words

        self.dfs(numberCharMap, digits, words, current, 0)

        return words