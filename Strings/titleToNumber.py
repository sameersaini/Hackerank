class Solution:
    def titleToNumber(self, s: str) -> int:
        if len(s) == 0:
            return 0

        s = s[::-1]
        ans = (ord(s[0]) - 64)

        for index, char in enumerate(s[1:]):
            val = (ord(char) - 64)
            ans += (val * 26 ** (index + 1))

        return ans
