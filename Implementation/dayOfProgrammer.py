#!/bin/python3

import math
import os
import random
import re
import sys

def checkLeap(year, isGreg):
    if isGreg:
        return ((year % 400 == 0) or (year % 4 == 0 and year % 100 != 0))
    else:
        return year % 4 == 0

# Complete the dayOfProgrammer function below.
def dayOfProgrammer(year):
    if year <= 1917 or year >= 1919:
        if (year <= 1917 and checkLeap(year, False)) or (year >= 1919 and checkLeap(year, True)):
            return "12.09." + str(year)
        else:
            return "13.09." + str(year)
    else:
        return "26.09.1918"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()
