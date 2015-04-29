M=10**9+7
for _ in range(int(input())):
    S=int(input())
    if S%20 == 0:
        print((42*(S//20)-2)%M)
    else:
        print((42*(S//20)+S%20*2)%M)