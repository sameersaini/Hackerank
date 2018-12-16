def getCombinations(result, combination, candidates, target, startIndex):
    if target == 0:
        print(sum(combination))
        result.append(combination[::])
        return

    for i in range(startIndex, len(candidates)):
        if candidates[i] > target:
            break

        combination.append(candidates[i])
        getCombinations(result, combination, candidates, target - candidates[i], i)
        combination.pop()


class Solution:
    def combinationSum(self, candidates, target):
        if len(candidates) == 0: return []

        candidates.sort()
        result = []
        combination = []
        getCombinations(result, combination, candidates, target, 0)

        return result
