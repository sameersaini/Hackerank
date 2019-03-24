"""
The idea is to create a graph of words and there is a edge between two words if the 2 words differ by one character only
The the problem is reduces to finding the length shortest path between begin and end word.
For this we can use, BFS from start word. If path does not exists then return 0 or retuen the length of shortest path
"""

import string

class Solution(object):
    def createGraph(self, wordList):
        words = set(wordList)
        ans = {}
        for word in (words):
            for j in range(len(word)):
                for char in string.ascii_lowercase:
                    new_word = word[:j] + char + word[j + 1:]
                    if new_word != word and new_word in words:
                        if word in ans:
                            ans[word].append(new_word)
                        else:
                            ans[word] = [new_word]

        return ans

    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if endWord not in wordList:
            return 0

        wordList.append(beginWord)
        adjList = self.createGraph(wordList)
        minDistance = len(wordList) + 1
        visited = {word: False for word in wordList}

        queue = [[beginWord, 1]]

        while len(queue) != 0:
            temp = queue.pop(0)
            word, length = temp[0], temp[1]
            if visited[word]:
                continue

            visited[word] = True

            if word == endWord:
                if length < minDistance:
                    minDistance = length

            if word in adjList:
                for w in adjList[word]:
                    queue.append([w, length + 1])

        if minDistance == len(wordList) + 1:
            return 0
        else:
            return minDistance
