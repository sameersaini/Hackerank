#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {
        int T,slength,i;
    scanf("%d",&T);
    for(i=0;i<T;i++)
        {
        int start,end,diff,sum=0;
        char str[10000];
        scanf("%s",str);
        slength=strlen(str);
        for(start=0,end=slength-1;start<end;start++,end--)
        {
            diff= abs((int)str[start]-(int)str[end]);
            sum +=diff;
        }
        printf("%d\n",sum);
    }
    
    
     
    return 0;
}
