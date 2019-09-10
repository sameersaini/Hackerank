"""
Reverse the entire string and then reverse the individual words
"""
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 0:
            return ""

        return " ".join([word[::-1] for word in s[::-1].strip().split(" ") if len(word) > 0])
