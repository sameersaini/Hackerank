#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {
    int i,t;long int k,ans;
    scanf("%d",&t);
        for(i=1;i<=t;i++)
        {
          scanf("%ld",&k);
        if(k%2==1)
            { 
            ans=(k/2)*(k/2+1);
            printf("%ld\n",ans);
        }
        else
            {
            ans=(k/2)*(k/2);
            printf("%ld\n",ans);
        }
    }
    return 0;
}