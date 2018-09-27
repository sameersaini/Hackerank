#!/bin/python3

import os

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c, k):
    n = len(c)
    e = 100
    i = 0
    while (i+k) % n != 0:
        nextJump = (i+k) % n
        if c[nextJump] == 1:
            e -= 3
        else:
            e -= 1
        i = nextJump
    else:
        if c[(i+k) % n] == 1:
            e -= 3
        else:
            e -= 1
    return e



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c, k)

    fptr.write(str(result) + '\n')

    fptr.close()
