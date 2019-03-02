def findPivot(arr, low, high):
    if low > high:
        return -1

    if low == high:
        return low

    mid = low + (high - low) // 2

    if mid < high and arr[mid] > arr[mid + 1]:
        return mid
    elif mid > low and arr[mid] < arr[mid - 1]:
        return mid - 1
    elif arr[low] >= arr[mid]:
        return findPivot(arr, low, mid - 1)
    else:
        return findPivot(arr, mid + 1, high)


def binarySearch(arr, low, high, target):
    if low > high:
        return -1

    mid = low + (high - low) // 2

    if arr[mid] == target:
        return mid
    if arr[mid] > target:
        return binarySearch(arr, low, mid - 1, target)
    else:
        return binarySearch(arr, mid + 1, high, target)


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        pivot = findPivot(nums, 0, len(nums) - 1)

        if pivot == -1:
            return binarySearch(nums, 0, len(nums) - 1, target)

        if nums[pivot] == target:
            return pivot

        if nums[0] <= target:
            return binarySearch(nums, 0, pivot, target)
        else:
            return binarySearch(nums, pivot + 1, len(nums) - 1, target)