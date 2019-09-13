class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0

        i = 1

        minIndex = 0
        maxIndex = 0
        profit = 0

        while i < len(prices):
            while i < len(prices) and prices[i] > prices[i - 1]:
                maxIndex = i
                i += 1

            if maxIndex > minIndex:
                profit += (prices[maxIndex] - prices[minIndex])

            minIndex = i
            i += 1

        return profit
