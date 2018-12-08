class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s

        ans = ''
        length = len(s)
        for i in range(numRows):
            firstJump = (numRows -1 -i) * 2
            secondJump = i * 2

            temp = i
            if temp < length : ans += s[temp]
            firstJumped = False
            secondJumped = False
            while temp < length:
                if firstJump == 0:
                    temp += secondJump
                    if temp < length : ans += s[temp]
                    continue
                elif secondJump == 0:
                    temp += firstJump
                    if temp < length : ans += s[temp]
                    continue

                if firstJump != 0 and not firstJumped:
                    temp += firstJump
                    if temp < length : ans += s[temp]
                    firstJumped = True
                    secondJumped = False
                    continue
                elif secondJump != 0 and not secondJumped:
                    temp += secondJump
                    if temp < length : ans += s[temp]
                    secondJumped = True
                    firstJumped = False
                    continue

        return ans