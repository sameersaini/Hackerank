#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
int gcd(int,int);
int main() {
            int t;
            scanf("%d",&t);
            int l,b,max;
    while(t--)
    {
    scanf("%d%d",&l,&b);
    int i;
    i=gcd(l,b);
    max=(l*b)/(i*i); 
    printf("%d\n",max); 
    }
    return 0;
}
int gcd(int a, int b)
    {int t;
    while(a)
        {
        t=b%a;
        b=a;
        a=t;
    }
     return b;
}