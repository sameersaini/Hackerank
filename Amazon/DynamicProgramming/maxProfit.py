"""
The idea is to initialize the minimum diff to first number and the keep on updating it as you find the smaller number
Then for every number keep on finding the diff from minimum number to see if it is larger than the largestDiff.
"""

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
            return 0

        largestDiff = 0
        mini = prices[0]

        for i in range(1, len(prices)):
            if prices[i] < mini:
                mini = prices[i]

            diff = prices[i] - mini
            if diff > largestDiff:
                largestDiff = diff

        return largestDiff

