#!/bin/python3

import math
import os
import random
import re
import sys


nm = input().split()
n = int(nm[0])
m = int(nm[1])
matrix = []
for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

str = ''.join([matrix[row][column] for column in range(m) for row in range(n)])
str = re.sub(r"(?<=[A-Za-z0-9])([!@#$%& ]+)(?=[A-Za-z0-9])", " ", str)
print(str, end='')