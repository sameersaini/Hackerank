#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {
        char a[81];
        scanf("%s",a);
        int l=strlen(a);
    int b=floor(sqrt(l));
    int c=ceil(sqrt(l));
    if(b*c<l)
        b++;
    char d[10][10];
    int i,j,k;
    k=0;
    for(i=0;i<b;i++)
        {
        for(j=0;j<c;j++)
            {
             d[i][j]=a[k++];
        }
     //   printf("b=%d c=%d\n",b,c);
    }
    for(i=0;i<c;i++)
        {
        for(j=0;j<b;j++)
            {
            if(d[j][i]>=97 && d[j][i]<=122)
                {
                printf("%c",d[j][i]);
            }
            
        }
        printf(" ");
    }
      
    
    return 0;
}
