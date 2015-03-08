T=int(input())
for _ in range(T):
    N=int(input())
    height=1
    if N > 0:
        cycle=1
        for _ in range(N):
            if cycle==1:
                height *= 2
                cycle=2
            else:
                height += 1
                cycle=1
    print(height)