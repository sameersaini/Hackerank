N,K=(int(x) for x in input().split())
Numbers=[int(x) for x in input().split()]

swap=0

for i in range(N):
    if swap==K:
        break
    else:
        index=Numbers.index(max(Numbers[i:]))
        if index == i:
            continue
        else:
            temp=Numbers[index]
            Numbers[index]=Numbers[i]
            Numbers[i]=temp
            swap +=1
        
    
for x in Numbers:print(x,end=' ')