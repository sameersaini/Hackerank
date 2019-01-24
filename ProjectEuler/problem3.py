def largestPrime(number):
    largest = 0

    while number % 2 == 0:
        number = number/2
        largest = 2

    for i in range(3, int(number ** 0.5), 2):
        if number % i == 0:
            number = number/i
            largest = i

    print("largest: ", largest)
    if number == 1:
        print(largest)
    else:
        print(number)


largestPrime(600851475143)