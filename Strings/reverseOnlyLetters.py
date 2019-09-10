class Solution(object):
    def valid(self, char):
        return (ord(char) >= 97 and ord(char) <= 122) or (ord(char) >= 65 and ord(char) <= 90)

    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        if len(S) == 0:
            return ""

        S = list(S)
        left = 0
        right = len(S) - 1
        while left < right:
            while left < len(S) and not self.valid(S[left]):
                left += 1

            while right >= 0 and not self.valid(S[right]):
                right -= 1

            if left < len(S) and right >= 0 and left < right:
                S[left], S[right] = S[right], S[left]

            left += 1
            right -= 1

        return "".join(S)
