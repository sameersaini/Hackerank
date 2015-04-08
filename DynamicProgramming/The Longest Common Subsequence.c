#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

void printseq(int a[],int b[],int,int);
int max(int,int);
int LCS[5002][5002];

int main() {
    int lengthx,lengthy,i,j;
    int x[5000],y[5000];
    scanf("%d%d",&lengthx,&lengthy);
    
    for(i=0;i<lengthx;scanf("%d",&x[i++]));
    
    for(j=0;j<lengthy;scanf("%d",&y[j++])); 
    
  
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
    i--;j--;
    printseq(x,y,i,j);
    
    return 0;
}

int max(int a,int b){
    if (a>b){return a;}
    else {return b;}
}

void printseq(int x[5000],int y[5000],int i,int j){
    if(i==0 || j==0){return;}
    else if(x[i-1]==y[j-1]){
        printseq(x,y,i-1,j-1);
        printf("%d ",x[i-1]);
    }
    else{
        if(LCS[i][j-1] > LCS[i-1][j]){
            printseq(x,y,i,j-1);
        }
        else{
            printseq(x,y,i-1,j);
        }
    }
    
}