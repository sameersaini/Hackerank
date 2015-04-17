from math import sqrt
def isPerfect(n):                       #here in the problem we need to check the toal points lying on the circumfrence
    sqroot=int(sqrt(n))                 #these total points should be less than the total police stations set up by
    if sqroot * sqroot == n:            #police.
        return True
    else:
        return False

T=int(input())

for _ in range(T):
    d,k=(int(x) for x in input().split())
    r=int(sqrt(d))                      #obtain radius of the city
    
    TotalPoints=0                       
      
    for Cor in range(1,r+1):            #for each point on the radius check it lies on the circumfrence or not
        if isPerfect(d-Cor*Cor):        #it can be checked by the formula of a point lying on the circle or not.
            TotalPoints +=4             #if the point lies on the circle than its 4 mirror points are also on circle.
    
    
    if TotalPoints <= k:                #check if total points are less then that of total polices stations to be set 
        print("possible")               #up by the police.
    else:
        print("impossible")