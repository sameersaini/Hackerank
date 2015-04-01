[N,K,Q]=[int(x) for x in input().split()]
Numbers=[int(x) for x in input().split()]

i=0
for _ in range(K):
    if i==0:
        i=N-1
    else:
        i -= 1
        
for _ in range(Q):
    q=int(input())
    if i+q < N-1:
        print(Numbers[i+q])
    else:
        print(Numbers[i+q-N])
        