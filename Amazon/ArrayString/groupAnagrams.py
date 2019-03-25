"""
The property of anagram words is that they all map to same sorted word.
So for every word, find its sorted word and then append the original word to the list
against the key of sorted word in the ans map.

Finally, return all the values in the ans map.
"""
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = {}

        for word in strs:
            sortedWord = "".join(sorted(word))

            if sortedWord in ans:
                ans[sortedWord].append(word)
            else:
                ans[sortedWord] = [word]

        return list(ans.values())
