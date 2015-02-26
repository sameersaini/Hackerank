#!/usr/bin/python3
def maxXor(l, r):
    maxi=0
    for x in range(l,r+1):
        for y in range(x,r+1):
            xor= x ^ y
            if (xor>maxi):
                maxi = xor
    return maxi
if __name__ == '__main__':
  l = int(input())
  r = int(input())
  print(maxXor(l, r))
