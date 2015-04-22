(R,C)=(int(x) for x in input().split())

if R%2 == 0:
    print((R-2)*5 +1 +(C-1)*2)
else:
    print((R-1)*5 +(C-1)*2)