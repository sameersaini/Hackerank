#!/bin/python3

import math
import os
import random
import re
import sys

def checkValidTriangle(a, b, c):
    if a + b <= c:
        return False
    if a + c <= b:
        return False
    if b + c <= a:
        return False
    return True

# Complete the maximumPerimeterTriangle function below.
def maximumPerimeterTriangle(sticks):
    triangles = {}
    i = 0
    while i < len(sticks) - 2:
        j = i + 1
        while j < len(sticks) - 1:
            k = j + 1
            while k < len(sticks):
                if checkValidTriangle(sticks[i], sticks[j], sticks[k]) and  (str(sticks[i]) + str(sticks[j]) + str(sticks[k])) not in triangles:
                    triangles[str(sticks[i]) + str(sticks[j]) + str(sticks[k])] = [sticks[i], sticks[j], sticks[k]]
                k += 1
            j += 1
        i += 1

    maxTri = []
    length = 0
    for k in triangles:
        perimeter = sum(triangles[k])
        if perimeter == length:
            maxTri.append(triangles[k])
        elif perimeter > length:
            maxTri = [triangles[k]]
            length = perimeter

    print(triangles)
    if len(maxTri) == 0:
        return [-1]
    elif len(maxTri) == 1:
        return sorted(maxTri[0])
    else:
        longestMax = 0
        longestMaxTri = []
        for triangle in maxTri:
            longest = max(triangle)
            if longest > longestMax:
                longestMaxTri = [triangle]
            elif longest == longestMax:
                longestMaxTri.append(triangle)

        if len(longestMaxTri) == 1:
            return sorted(longestMaxTri[0])
        else:
            # multiple triangles have longest length
            longestMin = 0
            longestMinTri = []
            for triangle in longestMaxTri:
                longest = min(triangle)
                if longest > longestMin:
                    longestMinTri = [triangle]
                elif longest == longestMin:
                    longestMinTri.append(triangle)

            return sorted(longestMinTri[0])


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    sticks = list(map(int, input().rstrip().split()))

    result = maximumPerimeterTriangle(sticks)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
