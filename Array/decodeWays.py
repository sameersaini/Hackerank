class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == "":
            return 0

        count = [0 for _ in range(len(s) + 1)]
        count[0] = 1
        count[1] = 1

        for i in range(2, len(count)):
            if s[i - 1] != '0':
                count[i] = count[i - 1]

            if s[i - 2] == '1' or (s[i - 2] == '2' and s[i - 2] < '7'):
                count[i] += count[i - 2]

        return count[-1]