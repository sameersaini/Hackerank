from collections import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        counts = Counter(s)

        length = 0

        for char in counts:
            if counts[char] % 2 == 0:
                length += counts[char]
            else:
                length += counts[char] - 1

        for char in counts:
            if counts[char] % 2 == 1:
                return length + 1

        return length