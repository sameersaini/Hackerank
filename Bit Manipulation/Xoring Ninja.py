t=int(input())
while t > 0:
    t -= 1
    total=int(input())
    numbers=[ int(x) for x in input().split()]
    ans=numbers[0]
    for i in numbers[1:]:
        ans=ans|i
    sum=ans*pow(2,total-1)    
    sum=sum%1000000007
    print(sum)