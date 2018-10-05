#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the weightedUniformStrings function below.
def weightedUniformStrings(s, queries):
    length = len(s)
    ans  = []
    counter = set(s)
    weights = {}
    weightsInS = {}
    length = len(s)
    for i in range(1,27): weights[chr(96+i)] = i
    for k in counter: weightsInS[k] = weights[k]

    weightValues = weightsInS.values()

    for query in queries:
        if query in weightValues:
            ans.append("Yes")
            continue
        #print("for query ", query)
        for weight in weightValues:
            #print("checking weight ", weight)
            if query % weight == 0:
                multiplier = query // weight
                if multiplier > length:
                    continue
                #print(multiplier)
                strToCheck = multiplier * chr(96+weight)
                #print("str to check is ", strToCheck)
                if strToCheck in s:
                    ans.append("Yes")
                    break
        else:
            ans.append("No")
    return ans


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input())
        queries.append(queries_item)

    result = weightedUniformStrings(s, queries)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
