from collections import Counter


class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """

        superSet = Counter(magazine)
        subSet = Counter(ransomNote)

        for char in subSet:
            if char not in superSet or superSet[char] < subSet[char]:
                return False

        return True