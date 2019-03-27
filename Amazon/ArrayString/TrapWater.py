class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) == 0:
            return 0

        totalWater = 0
        maxSeenLeft = [0 for _ in range(len(height))]
        maxSeenRight = [0 for _ in range(len(height))]

        maxSeenLeft[0] = height[0]
        maxSeenRight[-1] = height[-1]

        for i in range(1, len(height)):
            maxSeenLeft[i] = max(height[i], maxSeenLeft[i - 1])
            maxSeenRight[-i - 1] = max(height[-i - 1], maxSeenRight[-i])

        for i in range(len(height)):
            totalWater += min(maxSeenLeft[i], maxSeenRight[i]) - height[i]

        return totalWater