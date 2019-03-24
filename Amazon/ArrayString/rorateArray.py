"""
This is an implementation of juggling algorithm in which we divide the array into smaller sets
and the rotate the numbers in these chunks.
Number of sets = GCD(arrayLength, numberOfRotationsRequired)

"""

class Solution:
    def GCD(self, a, b):
        if b == 0:
            return a

        return self.GCD(b, a % b)

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 0:
            return

        n = len(nums)

        # this is for right rotate. For left rotate, k = k % n
        k = n - k % n
        gcd = self.GCD(n, k)

        for i in range(gcd):
            temp = nums[i]
            j = i

            while True:
                d = (j + k) % n
                if d == i:
                    break

                nums[j] = nums[d]
                j = d

            nums[j] = temp
