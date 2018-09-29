#!/bin/python3

import os
from collections import Counter

# Complete the equalizeArray function below.
def equalizeArray(arr):
    return len(arr) - sorted(list(Counter(arr).values()), reverse=True)[0]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = equalizeArray(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
