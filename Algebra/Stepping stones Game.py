import math
t=int(input())
while(t!=0):
    t=t-1
    n=int(input())
    num= 8*n + 1
    ans = int(math.sqrt(num))
    if(num == ans*ans):
        steps = (ans-1)//2
        print ("Go On Bob {}".format(steps))
    else:
        print("Better Luck Next Time")