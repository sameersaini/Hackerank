#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, steps):
    onSeaLevel = True
    upHill = False
    downHill = False
    valleysCrossed = 0
    level = 0

    for step in steps:
        if step == 'U':
            level += 1
        else:
            level -= 1

        if level > 0:
            upHill = True
            onSeaLevel = False
            downHill = False
        elif level < 0:
            upHill = False
            onSeaLevel = False
            downHill = True
        else:
            onSeaLevel = True

        if onSeaLevel and downHill:
            valleysCrossed += 1

    return valleysCrossed


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
