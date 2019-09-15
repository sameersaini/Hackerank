class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return -1

        firstLocation = {}
        charCount = {}
        minIndex = len(s) + 1

        for index, char in enumerate(s):
            if char not in charCount:
                charCount[char] = 1
                firstLocation[char] = index
            else:
                charCount[char] += 1

        for char in charCount:
            if charCount[char] == 1:
                minIndex = min(minIndex, firstLocation[char])

        if minIndex == len(s) + 1:
            return -1

        return minIndex