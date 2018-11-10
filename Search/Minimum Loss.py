#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumLoss function below.
def minimumLoss(prices):
    indexmap = {prices[i]: i for i in range(len(prices))}
    prices = sorted(prices)

    minDiff = 10**16
    for i in range(len(prices)-1):
        price1 = prices[i]
        price2 = prices[i+1]

        index1 = indexmap[price1]
        index2 = indexmap[price2]

        if index1 > index2:
            diff = price2 - price1
            if diff < minDiff:
                minDiff = diff
    return minDiff




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    price = list(map(int, input().rstrip().split()))

    result = minimumLoss(price)

    fptr.write(str(result) + '\n')

    fptr.close()
