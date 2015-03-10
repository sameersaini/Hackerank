#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {
    int t,n;int count;
    int rem,temp;
    scanf("%d",&t);
    while(t--)
        {
        count=0;
        scanf("%d",&n);
         temp=n;
        while(temp)
            {
            rem=temp%10;
            if(rem==0)
               {
                temp=temp/10;
                continue;
            }
            if(n%rem==0)
                {
               count++; 
            }
            temp=temp/10;
        }
         printf("%d\n",count);
    }
    return 0;
}