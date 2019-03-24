class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        length = len(nums)
        final = []
        for i in range(1 << length):
            ans = []
            for j in range(length):
                if (i & (1 << j)) > 0:
                    ans.append(nums[j])

            final.append(ans)

        return final
