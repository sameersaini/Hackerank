#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
#include <assert.h>
#include<stdio.h>
int insertionsort(int a[],int);
int main()
{

 int a[1000],s;
 scanf("%d",&s);
 int i;
for(i=0;i<s;scanf("%d ",&a[i++]));
insertionsort(a,s-1);    
return 0;
}
int insertionsort(int a[],int l)
{
 int i,j,v,k;
 for(i=1;i<=l;i++)
 {
  v=a[i];
  j=i;
  while(a[j-1]>v&&j>0)
  {
   a[j]=a[j-1];
   j--;
  }
 a[j]=v;
     for(k=0;k<=l;printf("%d ",a[k++]));
     printf("\n");
}
return 0;
}
 