#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the separateNumbers function below.
# algo is to start from smallest number and then generate its next number and then search it in the string till all the numbers are found.
# if this fails then repeat the step one for numbers of greater length.
# if no match is found till half length of string then return no.
def separateNumbers(s):
    ans = False
    for i in range(1, len(s)//2+1):
        number = int(s[0:i])
        found = True
        pos = i + 1
        next = number + 1
        while found:
            nextLength = len(str(next))
            if pos + nextLength - 1 <= len(s):
                check = s[pos-1: pos + nextLength-1]
                if int(check) == next:
                    next += 1
                    pos += nextLength
                else:
                    found = False
            else:
                break
        if found and pos >= len(s):
            print("YES " + s[0:i])
            return
    print("NO")
    return

if __name__ == '__main__':
    q = int(input())

    for q_itr in range(q):
        s = input()

        separateNumbers(s)
