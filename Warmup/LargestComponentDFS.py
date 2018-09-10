#!/bin/python3

import os

def safe(row, col, visited, arr):
    return row >= 0 and col >= 0 and row < len(arr) and col < len(arr[0]) and not visited[row][col] and arr[row][col] == 1

def DFS(row, col, arr, visited, count):
    rowNbr = [-1,-1,-1, 0, 1, 1, 1, 0]
    colNbr = [-1, 0, 1, 1, 1, 0,-1,-1]

    visited[row][col] = True

    for i in range(8):
        if safe(row + rowNbr[i], col + colNbr[i], visited, arr):
            count[0] += 1
            DFS(row + rowNbr[i], col + colNbr[i], arr, visited, count)

def maxRegion(arr):
    visited = [[False for _ in range(len(arr[0]))] for _ in range(len(arr))]
    result = -1

    for i in range(len(arr)):
        for j in range(len(arr[0])):
            count = [1]
            if not visited[i][j] and arr[i][j] == 1:
                DFS(i, j, arr, visited, count)
                result = max(result, count[0])
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    m = int(input())

    grid = []

    for _ in range(n):
        grid.append(list(map(int, input().rstrip().split())))

    res = maxRegion(grid)

    fptr.write(str(res) + '\n')

    fptr.close()
