#!/bin/python3

import os
import sys
from math import gcd

def checkFactor(number, arr):
    for x in arr:
        if x % number != 0:
            return False
    return True

def checkMultiple(number, arr):
    for x in arr:
        if number % x != 0:
            return False
    return True

def getTotalX(a, b):
    count = 0
    for possibleAns in range(max(a), min(b) + 1):
        if checkFactor(possibleAns, b) and checkMultiple(possibleAns, a):
            count += 1
    return count

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    total = getTotalX(a, b)

    f.write(str(total) + '\n')

    f.close()
