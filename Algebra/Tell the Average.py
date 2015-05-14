N=int(input())
L=[int(x) for x in input().split()]
first=L[0]
for i in range(1,len(L)):
    first = (first + L[i] + first*L[i])%1000000007
print(first)