#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {

    int a[100];
    int n,i,j;
    for(i=0;i<100;a[i++]=0);
    scanf("%d",&n);
    while(n--)
        {
        scanf("%d",&j);
        a[j]++;
    }
    for(i=0;i<100;printf("%d ",a[i++]));
    return 0;
}
