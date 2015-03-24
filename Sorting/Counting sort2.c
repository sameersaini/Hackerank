#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {

    int a[100];
    int n,i,j,k;
    for(i=0;i<100;a[i++]=0);
    scanf("%d",&n);
    i=n;
    while(n--)
        {
        scanf("%d",&j);
        a[j]++;
    }
    
    for(k=0;k<100;k++)
        {
        while(a[k])
            {
            printf("%d ",k);
            a[k]=a[k]-1;
        }
    }
    
    return 0;
}
