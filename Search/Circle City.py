"""
Problem Statement

Roy lives in a city that is circular in shape on a 2D plane that has radius r. The city center is located at origin (0,0) and it has suburbs lying on the lattice points (points with integer coordinates). The city Police Department Headquarters can only protect those suburbs which are located strictly inside the city. The suburbs located on the border of the city are still unprotected. So the police department decides to build at most k additional police stations at some suburbs. Each of these police stations can protect the suburb it is located in.

Given the square of radius, d(=r^2), of the city, Roy has to determine if it is possible to protect all the suburbs.

Input Format
The first line of input contains integer t; t test cases follow.
Each of the next t lines contains two space-separated integers: d, the square of the radius of the city, and k, the maximum number of police stations the headquarters is willing to build.

Constraints
1≤t≤103
1≤d≤2×109
0≤k≤2×109

Output Format
For each test case, print in a new line possible if it is possible to protect all the suburbs;, otherwise, print impossible.
"""
"""------------------------------------------------SOLUTION--------------------------------------------------------------------------------"""

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