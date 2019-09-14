class Solution:
    def convertToTitle(self, n: int) -> str:
        ans = ""

        while n != 0:
            remainder = n % 26
            n = n // 26

            if remainder == 0:
                remainder = 26
                n -= 1

            ans += chr(64 + remainder)

        return ans[::-1]