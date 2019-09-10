class Solution(object):
    def ispalindrome(self, s, left, right):
        while left < right:
            if s[left] != s[right]:
                return False

            left += 1
            right -= 1

        return True

    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        if len(s) == 0:
            return True

        left = 0
        right = len(s) - 1

        while left < right:
            if s[left] != s[right]:
                return self.ispalindrome(s, left + 1, right) or self.ispalindrome(s, left, right - 1)

            left += 1
            right -= 1

        return True
