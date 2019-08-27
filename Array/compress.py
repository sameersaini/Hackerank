class Solution:
    def compress(self, chars: List[str]) -> int:
        originalLength = len(chars)
        if originalLength == 0 or originalLength == 1:
            return originalLength
        counter = 1
        startIndex = 1
        for i in range(1, originalLength):
            if chars[i] == chars[i - 1]:
                counter += 1
            else:
                if counter == 1:
                    chars[startIndex] = chars[i]
                else:
                    for char in list(str(counter)):
                        chars[startIndex] = char
                        startIndex += 1

                    chars[startIndex] = chars[i]
                    counter = 1

                startIndex += 1

        if counter != 1:
            for char in list(str(counter)):
                chars[startIndex] = char
                startIndex += 1

        return startIndex

