T=int(input())
for _ in range(T):
    N=int(input())
    Grid=[list(input()) for _ in range(N)]
    for row in Grid:
        row.sort()
    flag=0
    for col in range(N):
        for row in range(1,N):
            if Grid[row-1][col] > Grid[row][col]:
                print("NO")
                flag=1
                break
        if flag:
            break
    else:
        print("YES")
    