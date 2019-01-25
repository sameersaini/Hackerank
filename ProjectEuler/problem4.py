number = 999 * 999

found = False
while number != 0:
    if str(number) == str(number)[::-1]:
        print(number)
        n = 999
        while n != 1:
            if number % n == 0 and number//n <= 999:
                found = True
                break
            n -= 1
        if found:
            break
    number -= 1
