#!/bin/python3

import os
from collections import Counter

# Complete the makeAnagram function below.
def makeAnagram(a, b):
    totalChars = len(a) + len(b)
    countA, countB = Counter(a), Counter(b)
    setA, setB = set(a), set(b)

    intersection = setA & setB
    AnaLength = 0
    for char in intersection: AnaLength += min(countA[char], countB[char])

    return totalChars - 2 * AnaLength


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()
