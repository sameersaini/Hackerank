import math
t=int(input())
while t>0:
    t -= 1
    
    (zeros,ones)=(int(x) for x in input().split())
    ones -= 1
    total=zeros + ones
    factTotal=math.factorial(total)
    factOnes=math.factorial(ones)
    factZeros=math.factorial(zeros)
    ans=(factTotal)//(factOnes * factZeros)
    ans=ans % (1000000007)
    print(ans)