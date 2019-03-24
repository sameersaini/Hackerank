"""
The solution is recursive where we have to maintain a cost matrix F[]
where F[i] represents the cost of jumping from index i and forward.

Therefore, for every index F[i] = cost[i] + min(F[i+1], F[i+2])

Finally, we return the min of (F[0], F[1])
"""

class Solution:
    def findCost(self, costMap, cost, index):
        if index >= len(costMap):
            return 0

        nextIndexVal = self.findCost(costMap, cost, index + 1)

        if index + 2 >= len(costMap):
            nextnextIndexVal = 0
        else:
            nextnextIndexVal = costMap[index + 2]

        val = cost[index] + min(nextIndexVal, nextnextIndexVal)
        costMap[index] = val

        return val

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        costMap = [0 for _ in range(len(cost))]

        self.findCost(costMap, cost, 0)

        return min(costMap[0], costMap[1])