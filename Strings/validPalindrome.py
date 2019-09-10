class Solution(object):
    def valid(self, char):
        return re.match(r'[a-z0-9]', char)

    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) == '':
            return True

        left = 0
        right = len(s) - 1
        s = s.lower()

        while left < right:

            while left < len(s) and not self.valid(s[left]):
                left += 1
            while right >= 0 and not self.valid(s[right]):
                right -= 1

            if left < len(s) and right >= 0 and s[left] != s[right]:
                return False

            left += 1
            right -= 1

        return True