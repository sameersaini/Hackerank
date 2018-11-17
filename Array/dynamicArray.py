#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the dynamicArray function below.
def dynamicArray(n, queries):
    ans = []
    lastAnswer = 0
    N = n
    arrs = [[] for _ in range(n)]

    for query in queries:
        x = query[1]
        y = query[2]
        if query[0] == 1:
            arrs[(x ^ lastAnswer) %  N].append(y)
        else:
            index = ((x ^ lastAnswer) %  N)
            lastAnswer = arrs[index][y % len(arrs[index])]
            ans.append(lastAnswer)
    return ans


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nq = input().rstrip().split()

    n = int(nq[0])

    q = int(nq[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
