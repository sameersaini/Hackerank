#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict

# Complete the sockMerchant function below.
def sockMerchant(n, arr):
    counter = defaultdict(int)
    for sock in arr: counter[sock] += 1
    return sum([counter[key]//2 for key in counter])

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
