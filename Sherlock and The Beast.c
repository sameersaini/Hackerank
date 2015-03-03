#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {
    int t,n,a,b;
    scanf("%d",&t);
    while(t--)
        {
        int flag=0;
        scanf("%d",&n);
        int i;
        int j;
        for(i=0;i<=n/5+1;i++)
            {
            for(j=0;j<=n/3+1;j++)
                {
                  if(n==(3*j + 5*i)) 
                  {
                      flag=1;
                      break ;
                  }
               }
             if(flag==1)
                {
                 break;
            }
        }
        if(flag==0)
            {
            printf("-1");
        }
        else
            {a=j*3;b=i*5;
            while(a--)
                printf("5");
            while(b--)
                printf("3");
                }
        
     printf("\n");   
    }
        
    return 0;
}
