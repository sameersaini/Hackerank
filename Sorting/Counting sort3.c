
#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {

    int a[100];char b[10];
    int n,i,j,k,count=0;
    for(i=0;i<100;a[i++]=0);
    scanf("%d",&n);
    i=n;
    while(n--)
        {
        scanf("%d%s",&j,b);
        a[j]++;
    }
    
    for(k=0;k<100;k++)
        {
        count=count+a[k];
        printf("%d ",count);
    }
    
    return 0;
}
