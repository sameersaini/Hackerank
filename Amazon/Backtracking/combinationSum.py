class Solution(object):
    def findCombinations(self, candidates, combinations, combination, startIndex, target):
        if target == 0:
            combinations.append(combination[::])

        for i in range(startIndex, len(candidates)):
            if candidates[i] > target:
                break

            combination.append(candidates[i])
            self.findCombinations(candidates, combinations, combination, i, target - candidates[i])
            combination.pop()

    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if len(candidates) == 0:
            return []

        candidates.sort()
        combinations = []
        combination = []
        startIndex = 0

        self.findCombinations(candidates, combinations, combination, startIndex, target)

        return combinations