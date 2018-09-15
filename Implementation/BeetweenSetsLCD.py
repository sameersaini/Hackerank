#!/bin/python3

import os
import sys
from math import gcd

def LCM(arr):
    lcm = a[0]
    for i in a[1:]:
        lcm = (lcm*i)//gcd(lcm, i)
    return lcm

def getTotalX(a, b):
    lcm = LCM(a)
    smallestB = min(b)
    possibleAns = []

    i=1
    while lcm*i <= smallestB:
        possibleAns.append(lcm*i)
        i += 1

    count = 0
    for ans in possibleAns:
        factor = True
        for x in b:
            if x % ans != 0:
                factor = False
                break
        if factor:
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
