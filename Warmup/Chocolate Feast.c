#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {

    int t, n, c, m;
    scanf("%d", &t);
    while ( t-- )
    {
        scanf("%d%d%d",&n,&c,&m);
        int answer = 0; 
        int wraper = n/c;
        answer=wraper;
        while(wraper>=m)
            {
                wraper=wraper-m;
                answer++;
                wraper++;
        }
        printf("%d\n",answer);
    }
    return 0;
}