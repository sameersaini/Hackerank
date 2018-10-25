#!/bin/python3

import os


# Complete the triplets function below.
def triplets(a, b, c):
    # need unique from each list in order to avoid duplicate triplets.
    a = sorted(list(set(a)))
    b = sorted(list(set(b)))
    c = sorted(list(set(c)))

    ans = 0
    ai = 0
    ci = 0
    # for each "number" in b, find the count of numbers which are less than equal to "number"
    for number in b:
        while ai < len(a) and a[ai] <= number: ai += 1
        while ci < len(c) and c[ci] <= number: ci += 1
        ans += (ai * ci)

    return ans


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    lenaLenbLenc = input().split()

    lena = int(lenaLenbLenc[0])

    lenb = int(lenaLenbLenc[1])

    lenc = int(lenaLenbLenc[2])

    arra = list(map(int, input().rstrip().split()))

    arrb = list(map(int, input().rstrip().split()))

    arrc = list(map(int, input().rstrip().split()))

    ans = triplets(arra, arrb, arrc)

    fptr.write(str(ans) + '\n')

    fptr.close()
