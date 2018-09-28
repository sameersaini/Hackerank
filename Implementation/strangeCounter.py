#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the strangeCounter function below.
def strangeCounter(t):
    n = 0
    while t > 3 * (pow(2, n+1) - 1):
        n += 1

    time = 3 * (pow(2, n) - 1) + 1
    value = 3 * pow(2, n)

    diff = t - time
    return value - diff

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    result = strangeCounter(t)

    fptr.write(str(result) + '\n')

    fptr.close()
