#!/bin/python3

import os

# Complete the howManyGames function below.
def howManyGames(p, d, m, s):
    series = []
    while p >= m and s > 0:
        s -= p
        if s > 0:
            series.append(p)
        p -= d

    ans = len(series)
    if s > 0:
        ans += s // m
    return ans


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    pdms = input().split()

    p = int(pdms[0])

    d = int(pdms[1])

    m = int(pdms[2])

    s = int(pdms[3])

    answer = howManyGames(p, d, m, s)

    fptr.write(str(answer) + '\n')

    fptr.close()
