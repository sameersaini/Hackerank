#include<stdio.h>

void quicksort(int a[],int,int,int);
int partition(int a[],int,int,int);
int main()
{

 int a[5000];
 int n;
 scanf("%d",&n);
 int i;
 for(i=0;i<n;scanf("%d",&a[i++]));
 quicksort(a,0,n-1,n-1);
return 0;
}

void quicksort(int a[],int low,int high,int size)
{
 int pivot;
 if(low<high)
 {
  pivot=partition(a,low,high,size);
  quicksort(a,low,pivot-1,size);
  quicksort(a,pivot+1,high,size);
 }
}

int partition(int a[],int l,int h,int s)
{
 int pivot=a[h];int temp;int k;
 int low=l;
 int high=l;
 while(high<=h)
 {
  while(a[high]>pivot)
      high++;
  temp=a[low];
  a[low]=a[high];
  a[high]=temp;
  high++;
  low++;
}
    
for(k=0;k<=s;printf("%d ",a[k++]));
printf("\n");
return low-1;
}
 
  