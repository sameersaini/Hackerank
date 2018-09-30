#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the happyLadybugs function below.
def happyLadybugs(b):
    counter = Counter(b)
    # If underscore is there, then swaps can be made
    if '_' not in counter.keys():
        #no underscore, only one color
        if len(b) == 1:
            return "NO"

        # if no underscore is there,
        # then the colors has to be in the req condition for bug to be happy.
        # check for NO conditions.
        for i in range(len(b)):
            if i == 0:
                if b[i] != b[i+1]:
                    return "NO"
            elif i == len(b) - 1:
                if b[i] != b[i-1]:
                    return "NO"
            elif b[i] == b[i-1] or b[i] == b[i+1]:
                continue
            else:
                return "NO"
        return "YES"
    else:
        # If underscore is there, then swaps can be made
        # here we check is there is a color with only one occurance for a break condition.
        for key in counter:
            if key != '_' and counter[key] == 1:
                return "NO"
        return "YES"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input())

    for g_itr in range(g):
        n = int(input())

        b = input()

        result = happyLadybugs(b)

        fptr.write(result + '\n')

    fptr.close()
