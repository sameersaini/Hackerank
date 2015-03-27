import operator
n=int(input())
D={}
for i in range(1,n+1):
    (t,d)=(int(x) for x in input().split())
    D[i]=t+d
for k,v in sorted(D.items(),key=operator.itemgetter(1)):
    print(k,end=' ')