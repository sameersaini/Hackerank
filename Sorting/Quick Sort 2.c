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
    
    return 0;
}
int partition(int a[],int l,int h)
    {//printf("l=%d h=%d\n",l,h);
     if(h==-1)
        return 0;
     int b[500],c[500];
     int pivot=a[l];
     int i,j,k,temp;
      for(i=1,j=0,k=0;i<=h;i++)
          {
          if(a[i]<pivot)
              b[j++]=a[i];
          else
              c[k++]=a[i];
      }
    //  for(i=0;i<j;printf("%d ",b[i++]));printf("\n");
    //  for(i=0;i<k;printf("%d ",c[i++]));printf("\n");
   partition(b,0,j-1);
   partition(c,0,k-1);
    int p,q;
    for(i=0,p=0;p<j;p++,i++)
        a[i]=b[p];
    a[i]=pivot;
    i++;
    for(q=0;q<k;q++,i++)
        a[i]=c[q];
    if(i!=1)
    {
        for(temp=0;temp<i;printf("%d ",a[temp++]));
        printf("\n");
    }
return 0;
}