#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hackerrankInString function below.
def hackerrankInString(s):
    main = [ c for c in "hackerrank"]
    visited = [ False for _ in range(len("hackerrank"))]

    for c in s:
        if c in main:
            if main.index(c) == 0: visited[0] = True
            elif c == 'a':
                if visited[0] and not visited[1] : visited[1] = True
                elif visited[6] and not visited[7]: visited[7] = True
            elif c == 'r':
                if visited[5]: visited[6] = True
                if visited[4]: visited[5] = True
            elif c == 'k':
                if visited[2] and not visited[3]: visited[3] = True
                elif visited[8]and not visited[9]: visited[9] = True
            else:
                if visited[main.index(c)-1] and not visited[main.index(c)]: visited[main.index(c)] = True
    if False in visited: return "NO"
    else: return "YES"



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = hackerrankInString(s)

        fptr.write(result + '\n')

    fptr.close()
