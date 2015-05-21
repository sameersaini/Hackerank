"""------------------------------Sherlock and MinMax-----------------------
Watson gives Sherlock an array A1,A2...AN.
He asks him to find an integer M between P and Q(both inclusive), such that,
 min {|Ai-M|, 1 = i = N} is maximised. If there are multiple solutions, print
 the smallest one.

Input Format
The first line contains N. The next line contains space separated N integers,
 and denote the array A. The third line contains two space separated integers 
 denoting P and Q.

Output Format
In one line, print the required answer.

Constraints
1 <= N <= 10^2
1 <= Ai <= 10^9
1 <= P <= Q <= 10^9 

---------------------------SOLUTION-----------------------------------------
As,P and Q range from 1 tp 10^9 ,so we can't use brute force.

A careful observation shows that the the answer to the Problem is P or Q or 
Mid=A[i] and A[i+1] for all i.

So,the Solution follows as:
1)we first sort the list A.
2)create a new list L.Add P to it;
3)Add mid of all A[i] and A[i+1] to list L,if the mid lies in between P and Q,both inclusive.
4)if mid is not divisible by 2 completely then add int(ind) and int(mid) + 1 to the list L.
5)Finally add Q to the List L.
6)Now,for every element j in L,find the min(abs(Ai-j)). and take the max of these min values.

"""

"""--------------------------------SOLUTION--------------------------------"""
N=int(input())
A=[int(x) for x in input().split()]
P,Q=(int(x) for x in input().split())
L=[]					
L.append(P)

A.sort()

i=0

while i+1<len(A):
    if (A[i]+A[i+1])//2 >= P and (A[i]+A[i+1])//2 <= Q:
        L.append((A[i]+A[i+1])//2)
    if (A[i]+A[i+1])%2 != 0:
        if (A[i]+A[i+1])//2 >= P and (A[i]+A[i+1])//2 <= Q:
            L.append((A[i]+A[i+1])//2 + 1)
    i += 1

L.append(Q)
MinMax=-1
index=0
for i in L:
    Temp=[]
    for j in A:
        Temp.append(abs(j-i))
    small=min(Temp)
    
    
    if small>MinMax:
        MinMax=small
        index=i

print(index)