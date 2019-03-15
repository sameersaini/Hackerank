"""
The idea is that the keep on adding the values in the array and then
for a continuous sub array having sum k, Sum(current index) - Sum(previous index) == k
if Sum == k, then maxLength = currentIndex + 1
Therefore, keep a map of Sum: index
Check if Sum(current index) - k is present in the map.
if yes, then maxLength = max(maxLength, currentIndex - index at Sum(current index) - k)
"""
class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        diffMap = {}

        sum = 0
        maxLength = 0

        for i in range(len(nums)):
            sum += nums[i]

            if sum == k:
                maxLength = i + 1

            if sum not in diffMap:
                diffMap[sum] = i

            if sum - k in diffMap:
                if maxLength < (i - diffMap[sum - k]):
                    maxLength = i - diffMap[sum - k]

        return maxLength
