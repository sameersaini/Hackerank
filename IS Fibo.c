#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {
    long int t,n,a,b,sum;
    scanf("%ld",&t);
    while(t--)
       {
        a=0;b=1;
        sum=0;
        scanf("%ld",&n);
        if(n==1)
        {
            printf("IsFibo\n");
            continue;
        }
        while(sum<=n)
            {
            
            sum=a+b;
            a=b;
            b=sum; 
            if(sum==n)
                {
                printf("IsFibo\n");
                break;
            }
        }
        if(sum>n)
            printf("IsNotFibo\n");
    }
    return 0;
}
