class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        if len(words) == 0:
            return True

        orderIndexes = {char: index for index, char in enumerate(order)}

        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]
            isWord1Small = False
            for index in range(min(len(word1), len(word2))):
                if orderIndexes[word1[index]] < orderIndexes[word2[index]]:
                    isWord1Small = True
                    break
                elif orderIndexes[word1[index]] > orderIndexes[word2[index]]:
                    return False
                else:
                    continue

            if isWord1Small:
                continue

            if len(word1) > len(word2):
                return False

        return True
