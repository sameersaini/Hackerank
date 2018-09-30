#!/bin/python3

import os
from collections import Counter

# Complete the minimumDistances function below.
def minimumDistances(arr):
    counter = Counter(arr)
    temp = []
    for k in counter:
        if counter[k] > 1: temp.append(k)

    indexes = {}
    for number in temp:
        indexes[number] = [i for i, val in enumerate(arr) if val == number]

    minimum = pow(10, 4)
    for key in indexes:
        l = indexes[key]
        for i in range(len(l)-1):
            if l[i+1] - l[i] < minimum:
                minimum = l[i+1] - l[i]

    if minimum == pow(10, 4):
        return -1

    return minimum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a)

    fptr.write(str(result) + '\n')

    fptr.close()
