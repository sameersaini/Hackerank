#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
int main() {
            char a[10000],b[10000];
            int c[26],d[26];
            int i;
            scanf("%s%s",a,b);
            for(i=0;i<(int)strlen(a);i++)
                c[a[i]-'a']++;
            for(i=0;i<(int)strlen(b);i++)
                d[b[i]-'a']++;
            int count=0;
            for(i=0;i<26;i++)
                {
                 if(c[i]==0 || d[i]==0)
                     count=count+c[i]+d[i];
                else
                    count=count+(abs(c[i]-d[i]));
            }
    printf("%d",count);
    return 0;
}
