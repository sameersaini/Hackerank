#!/bin/python3

import sys


def nSum(n):
    return (n * (n + 1)) // 2


t = int(input().strip())
n = []
for a0 in range(t):
    n = int(input().strip()) - 1

    ans = 3 * nSum(int(n / 3)) + 5 * nSum(int(n / 5)) - 15 * nSum(int(n / 15))
    print(int(ans))
