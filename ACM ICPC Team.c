#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {

    char a[500][500];
    int n,m;int i,j,k;
    scanf("%d%d",&n,&m);
    for(i=0;i<n;scanf("%s",a[i++]));
    int match,max,count;
    max=0;
    for(i=0;i<n-1;i++)
        {
        for(j=i+1;j<n;j++)
         {
             match=0;
             for(k=0;k<m;k++)
         {
                if(a[i][k]=='1'||a[j][k]=='1')
                match++;
                
         }
        //  printf ("max=%d match=%d",max,match);
         if(match>max)
        {
            max=match;
            count=0;
        }
        if(match==max)
        {   //printf("count=%d\n",count);
            count++;
        }
        }             
    }
       printf("%d\n",max);
       printf("%d\n",count);
       
            
          
            
    
    return 0;
}
      