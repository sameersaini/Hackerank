#!/bin/python3

import os

def combi(soFar, rest, target):
    if len(rest) == 0:
        if sum(soFar) == target: return 1
        else: return 0

    if sum(soFar) > target: return 0

    return combi(soFar + [rest[0]], rest[1:], target) + combi(soFar , rest[1:], target)


# Complete the powerSum function below.
def powerSum(X, N):
    pows = []
    x = 1
    while pow(x, N) <= X:
        pows.append(pow(x, N))
        x += 1
    return combi([], pows, X)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    X = int(input())

    N = int(input())

    result = powerSum(X, N)

    fptr.write(str(result) + '\n')

    fptr.close()
