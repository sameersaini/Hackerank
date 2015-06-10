import math

t=int(input())

for _ in range(t):
    N=int(input())
    R=int(input())
    
    N_R_1=math.factorial(N+R-1)
    r=math.factorial(R)
    N_1=math.factorial(N-1)
    
    result=(N_R_1)//(r * N_1)
    
    if(len(str(result))>9):
        print(result%(10**9))
    else:
        print(result)