class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) == 0:
            return 0

        totalWater = 0
        left_max = 0
        right_max = 0

        left = 0
        right = len(height) - 1

        while left < right:
            if height[left] < height[right]:
                if height[left] > left_max:
                    left_max = height[left]
                else:
                    totalWater += (left_max - height[left])
                left += 1
            else:
                if height[right] > right_max:
                    right_max = height[right]
                else:
                    totalWater += (right_max - height[right])
                right -= 1

        return totalWater
