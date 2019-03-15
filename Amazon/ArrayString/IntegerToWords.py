numberWordMap = {
    1: 'One',
    2: 'Two',
    3: 'Three',
    4: 'Four',
    5: 'Five',
    6: 'Six',
    7: 'Seven',
    8: 'Eight',
    9: 'Nine',
    10: 'Ten',
    11: 'Eleven',
    12: 'Twelve',
    13: 'Thirteen',
    14: 'Fourteen',
    15: 'Fifteen',
    16: 'Sixteen',
    17: 'Seventeen',
    18: 'Eighteen',
    19: 'Nineteen',
    20: 'Twenty',
    30: 'Thirty',
    40: 'Forty',
    50: 'Fifty',
    60: 'Sixty',
    70: 'Seventy',
    80: 'Eighty',
    90: 'Ninety'
}


class Solution:
    def toWord(self, num):
        ret = []
        if num // 100 >= 1:
            hundred = num // 100
            ret.append(numberWordMap[hundred])
            ret.append("Hundred")
            num = num % 100

        if num in numberWordMap:
            ret.append(numberWordMap[num])
            num = 0
        elif num // 10 >= 1:
            tens = num // 10
            ret.append(numberWordMap[tens * 10])
            num = num % 10

        if num > 0:
            ret.append(numberWordMap[num])

        return ret

    def numberToWords(self, num: int) -> str:
        ans = []
        if num == 0:
            ans.append("Zero")
        if num // 10 ** 9 >= 1:
            billion = num // 10 ** 9
            ans.append(numberWordMap[billion])
            ans.append("Billion")
            num = num % 10 ** 9

        if num // 10 ** 6 >= 1:
            millions = num // 10 ** 6
            ans += self.toWord(millions)
            ans.append("Million")
            num = num % 10 ** 6

        if num // 10 ** 3 >= 1:
            thousands = num // 10 ** 3
            ans += self.toWord(thousands)
            ans.append("Thousand")
            num = num % 10 ** 3

        ans += self.toWord(num)

        return " ".join(ans)
