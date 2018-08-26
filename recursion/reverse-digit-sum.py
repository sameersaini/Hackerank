#!/bin/python3
def superDigit(n):
    if len(str(n)) == 1: return n
    return superDigit(sum([int(x) for x in str(n)]))


if __name__ == '__main__':
    nk = input().split()
    n = nk[0]
    k = int(nk[1])

    actual = sum([int(x) for x in n]) * k
    result = superDigit(actual)
    print(result)