#!/bin/python3

import os
import sys
from math import ceil

#
# Complete the pageCount function below.
#
def pageCount(n, p):
    distanceFromStart = p - 1
    distanceFromEnd = n - p

    if distanceFromStart < distanceFromEnd:
        return ceil(distanceFromStart / 2)
    else:
        if n % 2 == 0: return ceil(distanceFromEnd / 2)
        else: return distanceFromEnd // 2

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = int(input())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()
