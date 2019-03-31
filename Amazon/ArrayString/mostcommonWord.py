"""
Algo:
    Convert to lowercase
    Filer out only a-z chars and spaces.
    split to words array and create a counter
    iterate over the counter to check max count word except banned words

"""

from collections import Counter


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        bannedSet = set(banned)
        paragraph = paragraph.lower()

        newParagraph = ''
        for char in paragraph:
            if (97 <= ord(char) <= 122) or char == " ":
                newParagraph += char
            else:
                newParagraph += " "

        wordCount = Counter(newParagraph.split(" "))
        max = 0
        maxWord = ""

        for word in wordCount:
            if word != "" and word not in bannedSet:
                if wordCount[word] > max:
                    max = wordCount[word]
                    maxWord = word

        return maxWord
