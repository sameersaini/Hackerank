#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the alternate function below.
def alternate(s):
    # find unique chars
    chars = list(set(s))
    # make pairs of the unique chars
    pairs = [[chars[i], chars[j]] for i in range(len(chars) - 1) for j in range(i+1, len(chars))]

    """
    # for each pair, filter the string which only contains chars in the pair.
    # the using a regex check if two consective chars exist in a string.
    # if not, then check the length of the string to find the max distance of the string.
    """
    maxLength = 0
    for pair in pairs:
        temp = ''
        for char in s:
            if char in pair:
                temp += char
        if re.search(r'(.)\1', temp) == None:   # r'(.)\1' checks if two conseccutive chars exist in a string.
            if len(temp) > maxLength:
                maxLength = len(temp)
    return maxLength


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    l = int(input().strip())

    s = input()

    result = alternate(s)

    fptr.write(str(result) + '\n')

    fptr.close()
