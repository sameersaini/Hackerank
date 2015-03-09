t=int(input())
for _ in range(t):
    N,K=(int(x) for x in input().split())
    StudentsPresent=0
    ArrivalTime=[int(x) for x in input().split()]
    for Time in ArrivalTime:
        if Time <=0:
            StudentsPresent += 1
            if StudentsPresent >= K:
                print("NO")
                break
    else:
        print("YES")