class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        totalLength = len(nums1) + len(nums2)

        if totalLength % 2 == 0:
            iterator = totalLength // 2 + 1
        else:
            iterator = (totalLength + 1) // 2

        first = 0
        second = 0
        arr = []
        for i in range(iterator):
            if first < len(nums1) and second < len(nums2):
                if nums1[first] < nums2[second]:
                    arr.append(nums1[first])
                    first += 1
                elif nums1[first] > nums2[second]:
                    arr.append(nums2[second])
                    second += 1
                else:
                    if first < second:
                        arr.append(nums1[first])
                        first += 1
                    else:
                        arr.append(nums2[second])
                        second += 1
            else:
                if first < len(nums1):
                    arr.append(nums1[first])
                    first += 1
                if second < len(nums2):
                    arr.append(nums2[second])
                    second += 1

        if totalLength % 2 == 0:
            return (arr[-1] + arr[-2]) / 2
        else:
            return arr[-1]