N=int(input())

Numbers=[int(x) for x in input().split()]

Numbers.sort()

small=20000001

for i in range(1,len(Numbers)):
    diff=abs(Numbers[i]-Numbers[i-1])
    if diff < small:
        small=diff
for i in range(1,len(Numbers)):
    if abs(Numbers[i]-Numbers[i-1]) == small:
        print("{} {}".format(Numbers[i-1],Numbers[i]),end=' ')