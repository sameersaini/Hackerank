P=int(input())
Q=int(input())
flag=0
for number in range(P,Q+1):
    
    square=number**2
    
    Lhalf=str(square)[:len(str(square))//2]
    Rhalf=str(square)[len(str(square))//2:] 
    
    if len(str(square)) == 1 :
        Lhalf='0'
    
    if int(Lhalf)+int(Rhalf) == number:
        print(number,end=' ')
        flag=1

if flag==0:
    print("INVALID RANGE")