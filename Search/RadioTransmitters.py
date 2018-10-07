#!/bin/python3

import os
from collections import Counter

# Complete the hackerlandRadioTransmitters function below.
def hackerlandRadioTransmitters(x, k):
    x.sort()
    c = Counter(x)
    i = 0
    ans = 0
    while i < len(x):
        temp = x[i] + k
        while i < len(x) and x[i] < temp:
            prev = x[i]
            i += 1
        i -= 1

        while temp != prev:
            if temp in c:
                break
            temp -= 1

        value = temp + k
        while i < len(x) and x[i] <= value: i += 1
        ans += 1
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    x = list(map(int, input().rstrip().split()))

    result = hackerlandRadioTransmitters(x, k)

    fptr.write(str(result) + '\n')

    fptr.close()
