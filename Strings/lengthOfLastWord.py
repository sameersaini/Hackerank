import re
class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        result = re.search(r'([a-zA-Z]+) *$', s)

        if result == None:
            return 0
        else:
            return len(result.group(1))
        """

        result = s.strip().split()

        if len(result) == 0:
            return 0
        else:
            return len(result[-1])
