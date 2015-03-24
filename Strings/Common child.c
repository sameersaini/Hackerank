#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int max(int,int);
int LCS[5002][5002];

int main() {
    char x[5000],y[5000];
    scanf("%s",x);
    scanf("%s",y);
 
    int i,j;
    int lengthx,lengthy;
    lengthx=strlen(x);
    lengthy=strlen(y);
    for(i=1;i<lengthx+1;i++){
        for(j=1;j<lengthy+1;j++){
            if (x[i-1]==y[j-1]){
                LCS[i][j]= 1 + LCS[i-1][j-1];
            }
            else{
                LCS[i][j] = max(LCS[i-1][j] , LCS[i][j-1]);
            }
        }
    }
    printf("%d",LCS[i-1][j-1]);
    return 0;
}

int max(int a,int b){
    if (a>b){return a;}
    else {return b;}
}