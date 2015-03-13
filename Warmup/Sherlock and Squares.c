#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {
        int t,a,b,k,l;int count=0;
        int i;
    scanf("%d",&t);
    while(t--)
       { count=0;
        scanf("%d%d",&a,&b);
        if(a>b)
            {
            a=a^b;
            b=a^b;
            a=a^b;
        }
        k=sqrt(b);l=sqrt(a);
   
        if(k==l&&(k*k==b || l*l==a))
            {
            count++;
           
            }
        else
            {
        if(l*l==a)
                count++;
        for(i=l;i<=k;i++)
            {
            if(i*i>a)
                count++;
        }
        }
        printf("%d\n",count);
    }  
    return 0;
}