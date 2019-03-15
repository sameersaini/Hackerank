"""
The idea is calculate two arrays: left and right
for every number left array will contain product of numbers left of the that number
for every number right array will contain product of numbers right of the that number
Then multiply left and right arrays to find the actual ans
"""
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1 for _ in range(len(nums))]
        left = [1 for _ in range(len(nums))]
        right = [1 for _ in range(len(nums))]

        lProd = 1
        rProd = 1
        for i in range(len(nums)):
            left[i] = lProd
            right[-i - 1] = rProd

            lProd *= nums[i]
            rProd *= nums[-i - 1]

        for i in range(len(nums)):
            ans[i] = left[i] * right[i]

        return ans