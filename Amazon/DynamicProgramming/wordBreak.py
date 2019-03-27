"""
This is a DP solution and we use an array of size len(s) + 1 to track the word boundaries.
isWordBreak[j] is True if for word boundaries i and j, isWordBreak[j] is True
and s[j:i] is in dictionary
Finally we return the last value in isWordBreak.
"""

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if len(s) == 0:
            return False

        isWordBreak = [False for _ in range(len(s) + 1)]
        isWordBreak[0] = True

        for i in range(len(s) + 1):
            for j in range(i):
                if not isWordBreak[j]:
                    continue

                if s[j:i] in wordDict:
                    isWordBreak[i] = True
                    break

        return isWordBreak[-1]
