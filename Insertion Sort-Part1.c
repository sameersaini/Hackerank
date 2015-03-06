#include<stdio.h>
int insertionsort(int a[],int);
int main()
{

 int a[1000],s;
  scanf("%d",&s);
 int i;
for(i=0;i<s;scanf("%d ",&a[i++]));
insertionsort(a,s-1);
for(i=0;i<s;printf("%d ",a[i++]));    
return 0;
}

int insertionsort(int a[],int l)
{
 int i,j,v,k;
 
  v=a[l];
  j=l;
  while(a[j-1]>v&&j>0)
  {
   a[j]=a[j-1];
   for(k=0;k<=l;printf("%d ",a[k++]));
      printf("\n");
   j--;
  }
 a[j]=v;
return 0;
}