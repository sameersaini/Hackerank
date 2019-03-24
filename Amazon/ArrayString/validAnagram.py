"""
The idea is to check for the number of unique character and then check whether count of each unique character is same.
"""

from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sCounter = Counter(s)
        tCounter = Counter(t)

        if len(sCounter.keys()) == len(tCounter.keys()):
            for key in sCounter:
                if key not in tCounter:
                    return False
                if tCounter[key] != sCounter[key]:
                    return False
            return True
        else:
            return False