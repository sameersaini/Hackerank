#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {
    int t,i;char a[100000];int count,flag;
    scanf("%d",&t);
    while(t--)
        {flag=0;
         scanf("%s",a);count=0;
         for(i=1;i<strlen(a);i++)
             {
              if(a[i]==a[i-1])
                  count++;     
         }
         
         printf("%d\n",count);
    }
    
    return 0;
}