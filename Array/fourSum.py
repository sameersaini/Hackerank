class Solution:
    def fourSum(self, nums, target):
        nums.sort()
        solDic = {}
        for i in range(len(nums) - 3):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            if nums[i] * 4 > target:
                break
            for j in range(i+1, len(nums) - 2):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                k = j + 1
                l = len(nums) - 1
                while k<l:
                    total = nums[i] + nums[j] + nums[k] + nums[l]
                    if  total == target and (str(sorted([nums[i], nums[j], nums[k], nums[l]]))) not in solDic:
                        solDic[str(sorted([nums[i], nums[j], nums[k] , nums[l]]))] = [nums[i], nums[j], nums[k], nums[l]]
                        l -= 1
                        k += 1
                    elif total > target:
                        l -= 1
                    else:
                        k += 1

        return list(solDic.values())

