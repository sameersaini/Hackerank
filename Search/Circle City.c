/*
Problem Statement

Roy lives in a city that is circular in shape on a 2D plane that has radius r. The city center is located at origin (0,0) and it has suburbs lying on the lattice points (points with integer coordinates). The city Police Department Headquarters can only protect those suburbs which are located strictly inside the city. The suburbs located on the border of the city are still unprotected. So the police department decides to build at most k additional police stations at some suburbs. Each of these police stations can protect the suburb it is located in.

Given the square of radius, d(=r2), of the city, Roy has to determine if it is possible to protect all the suburbs.

Input Format
The first line of input contains integer t; t test cases follow.
Each of the next t lines contains two space-separated integers: d, the square of the radius of the city, and k, the maximum number of police stations the headquarters is willing to build.

Constraints
1≤t≤103
1≤d≤2×109
0≤k≤2×109

Output Format
For each test case, print in a new line possible if it is possible to protect all the suburbs;, otherwise, print impossible.
*/





#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
int isPerfect(int);

int main() {

    int t,d,k;
    scanf("%d",&t);
    while(t-- > 0){
        int TotalPoints=0;
        scanf("%d%d",&d,&k);
        int radius=(int)sqrt(d);
        int i;
        for(i=1;i<=radius;i++){
            if(isPerfect(d-i*i)){
                TotalPoints += 4;
            }
        }
        if(TotalPoints <= k){
            printf("possible\n");
        }
        else{
            printf("impossible\n");
        }
    }
    return 0;
}

int isPerfect(int n){
    int sqroot=(int)sqrt(n);
    if (sqroot*sqroot==n){
        return 1;
    }
    else{
        return 0;
    }
}