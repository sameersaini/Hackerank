t=int(input())
while(t!=0):
    t=t-1
    num=int(input())
    if(num%2==1):
        print (2)
    else:
        if(num%4==0):
            print (3)
        else:
            print (4)
    