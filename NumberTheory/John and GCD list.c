#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
int gcd(int,int);
int lcm(int,int);
int main() {
            int t,n,i,j,temp,temp1,k;
            int a[1000],b[1001];
            scanf("%d",&t);
           
    while(t--)
        {
        scanf("%d",&n);
        for(i=0;i<n;scanf("%d",&a[i++])); 
        b[0]=a[0]; 
        for(i=0;i<n-1;i++)
            {
             b[i+1]=lcm(a[i],a[i+1]);
        }
    
    b[n]=a[n-1];
    for(i=0;i<=n;printf("%d ",b[i++]));
    printf("\n");
    }
    return 0;
}
int lcm(int a,int b)
    {
     return((a*b)/gcd(a,b));
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