#!/bin/python3

import os
def safe(row, col,  maxRow, maxcol, visited, arr):
    return (row >=0 and col >=0 and row < maxRow and col < maxcol and not visited[row][col] and (arr[row][col] == '.'  or arr[row][col] == '*'))

def DFS(row, col, arr, visited, maxRow, maxcol, num):
    rowNbr = [-1,  0, 0, 1]
    colNbr = [ 0, -1, 1, 0]

    if arr[row][col] == "*":
        return num

    if visited[row][col]:
        return 0
    visited[row][col] = True

    validNeighbor = 0
    for i in range(4):
        if safe(row + rowNbr[i], col + colNbr[i], maxRow, maxcol, visited, arr):
            validNeighbor += 1

    if validNeighbor > 1:
        num += 1

    neighborMaxs = [0,0,0,0]
    for i in range(4):
        if safe(row + rowNbr[i], col + colNbr[i], maxRow, maxcol, visited, arr):
            neighborMaxs[i] = DFS(row + rowNbr[i], col + colNbr[i], arr, visited, maxRow, maxcol, num)

    return max(neighborMaxs)

# Complete the countLuck function below.
def countLuck(matrix, k):
    visited = []
    startPos = []
    # create a visited array
    for i in range(len(matrix)):
        temp = []
        row = matrix[i]
        for j in range(len(row)):
            if row[j] == 'X':
                temp.append(True)
            elif row[j] == '.':
                temp.append(False)
            elif row[j] == 'M':
                startPos = [i, j]
                temp.append(False)
            else:
                destination = [i, j]
                temp.append(False)
        visited.append(temp)

    if DFS(startPos[0], startPos[1], matrix, visited, len(matrix), len(matrix[0]), 0) == k:
        return "Impressed"
    else:
        return "Oops!"




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        nm = input().split()

        n = int(nm[0])

        m = int(nm[1])

        matrix = []

        for _ in range(n):
            matrix_item = input()
            matrix.append(matrix_item)

        k = int(input())

        result = countLuck(matrix, k)

        fptr.write(result + '\n')

    fptr.close()
