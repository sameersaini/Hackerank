def getCombinations(result, combination, candidates, target, startIndex):
    if target == 0:
        c = combination[::]
        if c not in result: result.append(c)
        return

    for i in range(startIndex, len(candidates)):
        if candidates[i] > target:
            break

        combination.append(candidates[i])
        getCombinations(result, combination, candidates, target - candidates[i], i+1)
        combination.pop()


class Solution:
    def combinationSum2(self, candidates, target):
        if len(candidates) == 0: return []

        candidates.sort()
        result = []
        combination = []
        getCombinations(result, combination, candidates, target, 0)

        return result
