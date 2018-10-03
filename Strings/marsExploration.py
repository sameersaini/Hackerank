#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the marsExploration function below.
def marsExploration(s):
    length = len(s)
    repeats = length // 3
    ans = 0
    for i in range(repeats):
        message = s[i*3:i*3+3]
        if message[0] != 'S': ans += 1
        if message[1] != 'O': ans += 1
        if message[2] != 'S': ans += 1
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = marsExploration(s)

    fptr.write(str(result) + '\n')

    fptr.close()
