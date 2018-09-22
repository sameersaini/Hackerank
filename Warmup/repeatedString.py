#!/bin/python3

import os

# Complete the repeatedString function below.
def repeatedString(s, n):
    strLength = len(s)
    count = 0
    for char in s:
        if char == 'a': count += 1

    multiplier = n // strLength # number to complete multipliers of the given string.
    total = count * multiplier  # total occurances of char 'a' in the string.
    remaining = n - multiplier * strLength  # partial string to consider.

    for char in s[:remaining]:
        if char == 'a': total += 1   # processing partial string

    return total

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
