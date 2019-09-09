class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 == "0" or num2 == "0":
            return "0"

        if len(num1) < len(num2):
            num1, num2 = num2, num1

        productArr = []
        maxLength = 0
        for index, num in enumerate(num2[::-1]):
            num = int(num)
            string = ""

            i = len(num1) - 1
            carry = 0
            while i >= 0:
                temp = num * int(num1[i]) + carry
                carry = temp // 10
                string += str(temp % 10)

                i -= 1

            if carry != 0:
                string += str(carry)

            toAppend = string[::-1] + "".join(["0" for _ in range(index)])
            productArr.append(toAppend)

            if len(toAppend) > maxLength:
                maxLength = len(toAppend)

        ans = ""
        carry = 0
        for i in range(maxLength):

            temp = 0
            for num in productArr:
                if i < len(num):
                    temp += int(num[-1 - i])

            temp += carry
            carry = temp // 10
            temp = temp % 10

            ans += str(temp)

        if carry != 0:
            ans += str(carry)

        return ans[::-1]