#!/bin/python3

import os

# Complete the breakingRecords function below.
def breakingRecords(scores):
    smallest = highest = scores[0]
    minRecordBreaked = maxRecordBreaked = 0

    for score in scores[1:]:
        if score < smallest:
            smallest = score
            minRecordBreaked += 1
        elif score > highest:
            highest = score
            maxRecordBreaked += 1

    return [maxRecordBreaked, minRecordBreaked]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
