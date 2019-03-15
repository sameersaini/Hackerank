"""
The idea is maintain a matrix where an entry [i][j] shows that the string from i to j is a palindrome
every substring of length 1 is palindrome
then we fill the table for substrings of length 2
For every substring from length 3 or more
if str[i] == str[j] and table[i+1][j-1] == True
then set table[i][j] = True and update maxLength and startIndex = i
"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        table = [[False for _ in range(len(s))] for _ in range(len(s))]
        start = 0
        maxLength = 1

        for i in range(len(s)):
            table[i][i] = True

        for i in range(len(s) - 1):
            if s[i] == s[i + 1]:
                table[i][i + 1] = True
                maxLength = 2
                start = i

        for k in range(3, len(s) + 1):
            for i in range(len(s) - k + 1):
                j = i + k - 1
                if table[i + 1][j - 1] == True and s[i] == s[j]:
                    table[i][j] = True
                    if k > maxLength:
                        maxLength = k
                        start = i
        return s[start:start + maxLength]
