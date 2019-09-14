class Solution(object):
    def addCombinations(self, left, n, k, candidate, ans):
        if k == 0:
            ans.append(candidate[::])
            return

        for i in range(left, n + 1):
            candidate.append(i)
            self.addCombinations(i + 1, n, k - 1, candidate, ans)
            candidate.pop()

    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if k > n:
            return []

        ans = []
        self.addCombinations(1, n, k, [], ans)

        return ans