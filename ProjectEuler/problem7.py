def isPrime(n):
    toCheck = int(n ** 0.5)

    for i in range(2, toCheck+1):
        if n % i == 0:
            return False
    else:
        return True


primes = 0
number = 2

while True:
    if isPrime(number):
        primes += 1
    if primes == 10001:
        break

    number += 1

print(number)