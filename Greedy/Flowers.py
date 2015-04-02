N,K=(int(x) for x in input().split())

cost=[int(x) for x in input().split()]

mincost=0

cost.sort()
cost.reverse()

temp=K
bought=0

for x in cost:
    mincost += (bought+1)*x
    temp -= 1
    if temp == 0:
        temp=K
        bought += 1
        
print(mincost)