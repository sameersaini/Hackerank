for x in range(int(input())):
    R,C=(int(i) for i in input().split())
    large=[]
    for i in range(R):
        large.append(input())
    r,c=(int(i) for i in input().split())
    small=[]
    for i in range(r):
        small.append(input())
    i=0
    matching=0
    for line in large:
        if small[i] in line:
            i =i + 1
            matching=1
            if i < r:continue
        if matching == 1 and i != r:
            matching=0
            i=0
        if i == r:break
    if i==r:print("YES")
    else:print("NO")