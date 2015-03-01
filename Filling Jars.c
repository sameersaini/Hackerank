#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {

    long int n,m,add;
    scanf("%ld%ld",&n,&m);
    int a,b;
    long int sum=0;
    while(m--)
        {
        scanf("%d%d%ld",&a,&b,&add);
        sum=sum+((b-a+1)*add);
    }
    printf("%ld",sum/n);
    
    return 0;
}