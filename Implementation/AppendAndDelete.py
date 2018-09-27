#!/bin/python3

import os

# Complete the appendAndDelete function below.
def appendAndDelete(s, t, k):
    lenS = len(s)
    lenT = len(t)
    same = 0
    for i in range(min(lenS, lenT)):
        if s[i] != t[i]:
            break
        same = i

    if k >= lenS + lenT:
        return "Yes"

    deletions = lenS - 1 - same
    insertions = lenT - 1 - same

    if k == (insertions + deletions):
        return "Yes"
    elif insertions == 0 and (k-deletions) % 2 == 0:
        return "Yes"
    elif deletions == 0 and (k-insertions) % 2 == 0:
        return "Yes"
    else:
        return "No"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    t = input()

    k = int(input())

    result = appendAndDelete(s, t, k)

    fptr.write(result + '\n')

    fptr.close()
