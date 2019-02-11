number = 2**1000

numberStr = str(number)

print(numberStr)
sum = 0

for digit in numberStr:
    sum += int(digit)

print(sum)