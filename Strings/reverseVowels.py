class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 0:
            return ""

        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        s = list(s)
        left = 0
        right = len(s) - 1

        while left < right:
            while left < len(s) and s[left] not in vowels:
                left += 1

            while right > 0 and s[right] not in vowels:
                right -= 1

            if left < right:
                s[left], s[right] = s[right], s[left]

            left += 1
            right -= 1

        return "".join(s)
