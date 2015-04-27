from math import sqrt
(L,S1,S2)=(int(x) for x in input().split())
Relative_Speed=abs(S2-S1)
for _ in range(int(input())):
    q=int(input())
    distance=sqrt(2*(L**2))-sqrt(2*q)
    time=distance/Relative_Speed
    print("{:.20f}".format(time))