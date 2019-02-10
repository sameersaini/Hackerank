def problem14():
    maxLength = 0
    maxLengthGenerator = 1
    valueMap = {}
    for i in range(1, 10**6+1):
        c = getLength(i, valueMap)
        valueMap[i] = c
        if c > maxLength:
            maxLength = c
            maxLengthGenerator = i

    print(maxLengthGenerator)


def getLength(number, value_map):
    terms = 1

    while number != 1:
        if number % 2 == 0:
            number = number//2
        else:
            number = 3 * number + 1

        if number in value_map:
            return terms + value_map[number]

        terms += 1

    return terms


problem14()
