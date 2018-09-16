#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the birthday function below.
# sliding window solution
def birthday(chocolates, d, m):
    if len(chocolates) < m: return 0

    count = 0
    total = sum(chocolates[:m])
    if total == d: count += 1

    for i in range(m, len(chocolates)):
        total = total + chocolates[i] - chocolates[i-m]
        if total == d: count += 1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    dm = input().rstrip().split()

    d = int(dm[0])

    m = int(dm[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()
