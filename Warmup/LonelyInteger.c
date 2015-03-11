#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
#include <assert.h>
int main() {
    int n;
    scanf("%d",&n);
    int a[100],b[100];
    int i,j;int count;
    for(i=0;i<n;scanf("%d",&a[i++]));
    for(i=0;i<n;i++)
        {count=0;
        for(j=0;j<n;j++)
            {
            if(a[i]==a[j])
                count++;
        }
        if(count==1)
            {
            printf("%d",a[i]);
            break;
        }
        } 
    
    
    return 0;
}