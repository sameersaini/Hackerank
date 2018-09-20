#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the pickingNumbers function below.
def pickingNumbers(a):
    ans = 0
    counter = [ 0 for _ in range(101)]
    for number in a: counter[number] += 1

    for i in range(len(counter)-1):
        neighborSum = counter[i] + counter[i+1]
        if neighborSum > ans:
            ans = neighborSum
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
