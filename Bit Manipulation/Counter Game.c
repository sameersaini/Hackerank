#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {
           int t,count; unsigned long n,i;
    scanf("%d",&t);
    while(t--)
        {
        count=0;
        scanf("%lu",&n);
        while(n!=1)
            {
             count++;//printf("%d\n",(n&&n-1));
             if(n&n-1)
                 {
                  for(i=1;n>(i << 1)&&i!=pow(2,63);i=i<<1);
                  n-=i;
                 }
            else
                {
                 n=n/2;
                }
                 
            }
        if(count%2)
            {
             printf("Louise\n");
            }
        else
            printf("Richard\n");
      }
return 0;
}
