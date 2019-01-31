def numberOfPrimes(number):
    primes = {}
    actual = number
    while number % 2 == 0:
        number = int(number/2)
        if 2 in primes:
            primes[2] += 1
        else:
            primes[2] = 1

    for i in range(3, int(actual ** 0.5)+1, 2):
        while number % i == 0:
            number = int(number/i)
            if i in primes:
                primes[i] += 1
            else:
                primes[i] = 1

    if number != 1:
        primes[number] = 1

    total = 1
    for key in primes:
        total = total * (primes[key]+1)

    return total


n = 1
d = 1
while numberOfPrimes(d) < 500:
    n += 1
    d += n


print(d)