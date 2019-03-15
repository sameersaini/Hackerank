class Solution:
    def firstUniqChar(self, s: str) -> int:
        firstCharLoc = {}
        charsMap = {}
        uniqueChars = []

        for index, char in enumerate(s):
            if char not in charsMap:
                charsMap[char] = 1
                firstCharLoc[char] = index
                uniqueChars.append(char)
            else:
                charsMap[char] += 1

        for char in uniqueChars:
            if charsMap[char] == 1:
                return firstCharLoc[char]
        else:
            return -1
