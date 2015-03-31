N=int(input())
Numbers=[int(x) for x in input().split()]

Numbers.sort()

print(Numbers[N//2])