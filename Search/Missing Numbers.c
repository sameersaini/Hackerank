#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {
        int m,n;int i,temp;
        int a[10001],b[10001];
        for(i=0;i<10001;i++)
            {
             a[i]=0;b[i]=0;
        }
      scanf("%d",&n);
    for(i=0;i<n;i++)
        {
         scanf("%d",&temp);
         a[temp]++;
    }
    scanf("%d",&m);
    for(i=0;i<m;i++)
        {
         scanf("%d",&temp);
         b[temp]++;
    }
    for(i=0;i<10001;i++)
        {
        if(a[i]!=b[i])
            printf("%d ",i);
    }
    return 0;
}
