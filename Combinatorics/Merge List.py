"""
Merge List is simply a problem of arranging N and M objects in a row,which can simply be obtained by calculating N+M C N i.e using combinations
"""
from math import factorial
for _ in range(int(input())):
    (N,M)=(int(x) for x in input().split())
    
    Total_Fact=factorial(N+M)
    N_Fact=factorial(N)
    M_Fact=factorial(M)
   
    print( (Total_Fact)//(N_Fact * M_Fact)% (10**9+7))