
#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
int main() {
int t;
scanf("%d",&t);
int n,a,b;    
    while(t--)
        {
        scanf("%d%d%d",&n,&a,&b);
        int i,temp;long int sum;
        if(a==b)
            {
            printf("%d \n",(n-1)*a);
        }
        else
            {
            if(a>b)
                {
                a=a^b;
                b=a^b;
                a=a^b;
            }
            for(i=0,temp=n;i<n;i++)
            {
            temp--;
            sum=temp*a + i*b;
            printf("%ld ",sum);
        }
        printf("\n");
        }
    }
return 0;
}