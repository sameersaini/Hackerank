#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the isValid function below.
def isValid(s):
    # create a counter of string characters and thier corresponding counts
    cntr = Counter(s)
    # fetch unique counts
    unique = list(set(list(cntr.values())))
    # create a counter of counts.
    cntr = Counter(list(cntr.values()))

    # if uniq counts is of length 1 then it means all characters in the string have same frequency
    if(len(unique) == 1):return "YES"
    # if uniq counts is of length more than 2,
    # then it means removing any one type character will not help solve the problem
    if(len(unique) > 2): return "NO"

    # For length of unique counts equal to 2
    # check if after removing one character of count 1 will leave the string with equal occurances
    uniqA, uniqB = unique[0], unique[1]
    if cntr[uniqA] == 1 or cntr[uniqB] == 1:
        if cntr[uniqA] == 1 and (uniqA-1 == 0 or uniqA-1 == uniqB):
            return "YES"
        elif cntr[uniqB] == 1 and (uniqB-1 == 0 or uniqB-1 == uniqA):
            return "YES"

    return "NO"



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
