#!/bin/python3

import math
import os
import random
import re
import sys

"""
Mainitain a hashmap of all the values seen so far with value as key and index as value
for every value, find its diffrence with money and see if the diff is present in the hashmap
if the diffrence is present in the hashmap, then the solution is found.
NOTE: do not create a hashmap upfront as it will override the duplicate values.
"""
def whatFlavors(cost, money):
    hash = {}

    for i in range(len(cost)):
        flavorPrice = cost[i]
        diff = money - flavorPrice

        if diff > 0 and diff in hash:
            print(*sorted([i+1 , hash[diff] + 1]))
            break
        else:
            hash[flavorPrice] = i

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        money = int(input())

        n = int(input())

        cost = list(map(int, input().rstrip().split()))

        whatFlavors(cost, money)
