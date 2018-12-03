class Solution:
    """
    Find nth term of sequence
    1.     1
    2.     11
    3.     21
    4.     1211
    5.     111221
    """
    def countAndSay(self, n):
        arr = [1]

        for i in range(1, n):
            number = arr[i-1]
            string = str(number)

            j = 1
            char = string[0]
            length = 1
            ans=''
            while j < len(string):
                if string[j] == string[j-1]:
                    length += 1
                else:
                    ans += (str(length) + string[j-1])
                    length = 1
                j += 1

            ans += (str(length) + string[j-1])
            arr.append(ans)

        return str(arr[n-1])