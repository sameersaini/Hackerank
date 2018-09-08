#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the primality function below.
def primality(n):
    sqrtN = math.sqrt(n)
    if n == 1:
        return "Not prime"
    for i in range(2, math.ceil(sqrtN)+1):
        if n % i == 0 and n != i:
            return "Not prime"
    else:
        return "Prime"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    p = int(input())

    for p_itr in range(p):
        n = int(input())

        result = primality(n)

        fptr.write(result + '\n')

    fptr.close()
