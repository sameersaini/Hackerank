#!/bin/python3

import os

def superReducedString(s):
    i = 0
    length = len(s)

    while len(s) > 0 and i < length-1:
        if s[i] == s[i+1]:
            s = s[:i] + s[i+2:]
            i = 0
            length = length - 2
        else:
            i += 1

    if len(s) == 0:return "Empty String"
    else:return s

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = superReducedString(s)

    fptr.write(result + '\n')

    fptr.close()
