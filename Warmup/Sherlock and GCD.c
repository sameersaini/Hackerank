#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
int gcd(int,int);
int main() {
            int t,n,i,j,k;int a[100];
        scanf("%d",&t);
        while(t--)
            {
            int i,n,g,a;
            scanf("%d",&n);
            scanf("%d",&g);
            for(i=1;i<n;i++)
                {
                scanf("%d",&a);
                g=gcd(a,g);
            }
             g>1 ? printf("NO\n") : printf("YES\n"); 
        }
return 0;
}
int gcd (int a,int g)
    {
    int i;   
        while(g){
            i=g;
            g=a%i;
            a=i;
        }
        
    return a;
}