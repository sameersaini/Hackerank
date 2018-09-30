#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the fairRations function below.
def fairRations(B):
    indexes = [i for i, number in enumerate(B) if number%2 == 1]

    if len(indexes)%2 == 1:
        return "NO"

    i = 0
    ans = 0
    while i < len(indexes):
        ans += 2 * (indexes[i+1] - indexes[i])
        i += 2
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    N = int(input())

    B = list(map(int, input().rstrip().split()))

    result = fairRations(B)

    fptr.write(str(result) + '\n')

    fptr.close()
