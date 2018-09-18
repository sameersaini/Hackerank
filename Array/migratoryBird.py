#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict

# Complete the migratoryBirds function below.
def migratoryBirds(arr):
    counter = defaultdict(int)
    for bird in arr: counter[bird] += 1

    max = -1
    maxArr = []
    for key in counter:
        if counter[key] == max:
            maxArr.append(key)
        elif counter[key] > max:
            max = counter[key]
            maxArr = [key]

    return sorted(maxArr)[0]




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
