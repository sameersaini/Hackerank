"""
The idea is to use a greedy approach
Here, we first record the last occurrence of each char in the string.

The we use two pointers start and end to maintain the current partition boundary.
For every character we keep on checking the last index of that character and
if it is more than the current end boundary, then we extend the end boundary.

If end boundary is equal to the current index, then we add the size of the current partition
to the ans array and set the start pointer to end + 1
"""


class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        lastIndexMap = {char: i for i, char in enumerate(S)}

        start = 0
        end = 0
        ans = []
        for i in range(len(S)):
            end = max(end, lastIndexMap[S[i]])

            if end == i:
                ans.append(end - start + 1)
                start = end + 1

        return ans

