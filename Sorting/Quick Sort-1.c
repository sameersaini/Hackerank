#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
#include <assert.h>
int partition(int a[],int,int);
int main(){
    int n,a[1000];
    scanf("%d",&n);
    int i,j,k;
    for(i=0;i<n;scanf("%d",&a[i++]));
    partition(a,0,n-1);
    for(k=0;k<n;printf("%d ",a[k++]));
    return 0;
}
int partition(int a[],int l,int h)
    {
     int b[500],c[500];
     int pivot=a[0];
     int i,j,k;
      for(i=1,j=0,k=0;i<=h;i++)
          {
          if(a[i]<pivot)
              b[j++]=a[i];
          else
              c[k++]=a[i];
      }
    int p,q;
    for(i=0,p=0;p<j;p++,i++)
        a[i]=b[p];
    a[i]=pivot;
    i++;
    for(q=0;q<k;q++,i++)
        a[i]=c[q];
return 0;
}