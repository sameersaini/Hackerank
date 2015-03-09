def findNthpower(M,n):
    if n == 1:
        return M
    R = findNthpower(M,n//2)
    R = multiplymatrix(R,R)
    if n%2 ==1:
        R = multiplymatrix(R,M)
    return R
def multiplymatrix(A,B):
    x=(((A[0][0]*B[0][0])%1000000007)+((A[0][1]*B[1][0])%1000000007))%1000000007
    y=(((A[0][0]*B[0][1])%1000000007)+((A[0][1]*B[1][1])%1000000007))%1000000007
    z=(((A[1][0]*B[0][0])%1000000007)+((A[1][1]*B[1][0])%1000000007))%1000000007
    w=(((A[1][0]*B[0][1])%1000000007)+((A[1][1]*B[1][1])%1000000007))%1000000007
    F=[[x,y],
       [z,w]]
    return F

t=int(input())
for _ in range(t):
    f0,f1,n=(int(x) for x in input().split())
    f2=f0+f1
    F=[[f2,f1],
       [f1,f0]]
    A=[[1,1],
       [1,0]]
    if n==1:print(f1%1000000007);continue
    if n==2:print(f2%1000000007);continue
    ApowerN=findNthpower(A,n)
    print((multiplymatrix(ApowerN,F))[1][1])