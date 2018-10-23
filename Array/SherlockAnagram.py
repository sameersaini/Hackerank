#!/bin/python3

import os
from collections import defaultdict


# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(s):
    mp = defaultdict(int)
    for i in range(len(s)):
        freq = [0] * 26
        for j in range(i, len(s)):
            freq[ord(s[j]) - ord('a')] += 1;
            mp[repr(freq)] += 1;
    ans = 0
    for key in mp:
        ans += (mp[key] * (mp[key] - 1)) // 2
    return ans



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()
