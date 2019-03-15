class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diffIndexMap = {}

        for i in range(len(nums)):
            if target - nums[i] in diffIndexMap:
                return [diffIndexMap[target - nums[i]], i]

            diffIndexMap[nums[i]] = i
