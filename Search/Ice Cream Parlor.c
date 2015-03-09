#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {
            int t,m,n,c[10000];
            int i,j,flag,sum;
    scanf("%d",&t);
    while(t--)
        {
        scanf("%d%d",&m,&n);
        for(i=0;i<n;scanf("%d",&c[i++]));
         for(i=0;i<n;i++)
            {
             for(j=i+1;j<n;j++)
                {
                sum=c[i]+c[j];
                if(sum==m)
                {   
                    break;
                    
                }
                
                }
             if(sum==m)
                 break;
            }
        printf("%d %d\n",i+1,j+1);
        
    }
    return 0;
}
