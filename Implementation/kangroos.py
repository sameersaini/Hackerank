#!/bin/python3

import os

# Complete the kangaroo function below.
def kangaroo(x1, v1, x2, v2):
    startingPoints = [x1, x2]
    speeds = [v1, v2]

    if startingPoints[0] > startingPoints[1]:
        catcher = 1
        ahead = 0
    elif startingPoints[0] == startingPoints[1]:
        if speeds[0] == speeds[1]: return "YES"
        else: return "NO"
    else:
        catcher = 0
        ahead = 1

    speedDiff = speeds[catcher] - speeds[ahead]
    distanceToCatch = startingPoints[ahead] - startingPoints[catcher]

    if speedDiff <= 0: return "NO"
    else:
        if distanceToCatch % speedDiff == 0: return "YES"
        else: return "NO"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    x1V1X2V2 = input().split()

    x1 = int(x1V1X2V2[0])

    v1 = int(x1V1X2V2[1])

    x2 = int(x1V1X2V2[2])

    v2 = int(x1V1X2V2[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()
