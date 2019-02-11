store = {
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
    20: 'twenty',
    30: 'thirty',
    40: 'forty',
    50: 'fifty',
    60: 'sixty',
    70: 'seventy',
    80: 'eighty',
    90: 'ninety',
    100: 'hundred',
    1000: 'one thousand'
}


totalChars = 0
for number in range(1, 1001):
    temp = number
    word = ''
    if number == 1000:
        word = store[number]
    elif number < 1000:
        isGreaterThanHundred = False
        isGreaterThanTen = False
        if number // 100 > 0:
            isGreaterThanHundred = True
            hundreds = number//100
            number = number % 100
            word += store[hundreds] + ' hundred'

        if number // 10 > 0:
            isGreaterThanTen = True
            tens = number // 10 * 10
            number = number % 10
            if isGreaterThanHundred:
                if tens + number in store:
                    word += ' and ' + store[tens + number]
                    number = 0
                else:
                    word += ' and ' + store[tens] + ' '
            else:
                if temp in store:
                    word += store[temp]
                    number = 0
                else:
                    word += store[tens] + ' '

        if number > 0:
            if isGreaterThanHundred and not isGreaterThanTen:
                word += ' and ' + store[number]
            else:
                word += store[number]

    totalChars += len(word.replace(" ", ""))

print(totalChars)