class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        longest = 0

        charMap = {}
        currLength = 0
        currentStr = ''

        for char in s:
            if char not in charMap:
                currLength += 1
                currentStr += char
                charMap[char] = 1
                if currLength > longest:
                    longest = currLength
            else:
                if currLength > longest:
                    longest = currLength
                currLength = 1
                charMap = {char: 1}
                temp = ''
                #print(currentStr)
                for c in currentStr[::-1]:
                    if c not in charMap:
                        charMap[c] = 1
                        currLength += 1
                        temp += c
                    else:
                        break
                currentStr = temp[::-1] + char
                if currLength > longest:
                    longest = currLength

        #print(currentStr)
        return longest