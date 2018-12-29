class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if digits[-1] == 9:
            i = -1
            while True:
                digits[i] = 0
                # check for first digit i.e. case of 9,9,9,...
                if len(digits) + (i - 1) < 0:
                    digits = [1] + digits
                    break


                digits[i-1] += 1

                if digits[i-1] == 10:
                    i = i - 1
                else:
                    break
        else:
            digits[-1] += 1

        return digits