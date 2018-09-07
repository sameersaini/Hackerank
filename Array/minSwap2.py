#!/bin/python3

import os

"""
This can be easily done by visualizing the problem as a graph. We will have n nodes and an edge directed from node i to node j if the element at i’th index must be present at j’th index in the sorted array.
The graph will now contain many non-intersecting cycles. Now a cycle with 2 nodes will only require 1 swap to reach the correct ordering, similarly a cycle with 3 nodes will only require 2 swap to do so.
"""
def minimumSwaps(arr):
    # Create a structure to save the array element along with the original index
    Arr = []
    for i in range(len(arr)): Arr.append([arr[i], i])

    # sort the array according to the value,
    # so that the values are in the required sorted order.
    Arr.sort(key=lambda a: a[0])

    # create a array of size n to keep track of elements visited in the cycles.
    visited = [False for _ in range(len(arr))]

    swaps = 0
    for i in range(len(arr)):
        # if visited or already at right position
        if visited[i] == True or Arr[i][1] == i: continue
        cycle = 0
        j = i
        # move thru the cycle and keep track of the length of the cycle.
        while visited[j] == False:
            visited[j] = True
            j = Arr[j][1]
            cycle += 1
        swaps += (cycle - 1) #number of swaps required are one less than the cycle length
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
