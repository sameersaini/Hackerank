#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {
            int t,n,a[100000];
            int i;long int suml,sumr,sum;
            
            int j,k;
    scanf("%d",&t);
   while(t--)
        {
        sum=0;sumr=0;
        scanf("%d",&n);
        for(i=0;i<n;scanf("%d",&a[i++]));
        suml=0;sumr=0;
        i=0;j=n-1;
        while(j-i>=1)
            {
             if(suml>=sumr)
                 sumr+=a[j--];
             else
                suml+=a[i++];            
        }
       if(sumr==suml)
           printf("YES\n");
       else
           printf("NO\n");
   } 
    return 0;
}