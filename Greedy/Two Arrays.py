T=int(input())

for _ in range(T):
    N,K=(int(x) for x in input().split())
    A=[int(x) for x in input().split()]
    B=[int(x) for x in input().split()]
    
    A.sort()
    B=sorted(B)[::-1]
    
    for i in range(len(A)):
        if A[i]+B[i] < K:
            print("NO")
            break
    else:
        print("YES")
    
    