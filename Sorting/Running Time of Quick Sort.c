#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
void insertionsort(int a[],int);
    
void quicksort(int a[],int,int,int);
int partition(int a[],int,int,int);

int countquick,countinsertion;

int main()
{

 int a[1000],b[1000];int c;
 int n;
 scanf("%d",&n);
 int i;
    
 for(i=0;i<n;scanf("%d",&a[i++]));
 for(i=0;i<n;b[i]=a[i],i++);
    
 quicksort(a,0,n-1,n-1);
 insertionsort(b,n);
    
printf("%d",countinsertion-countquick);
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
  countquick++;
  high++;
  low++;
}
return low-1;
}
void insertionsort(int a[],int n)
{
 int i=1;int j,k;
 while(i<n)
 {
  int temp=a[i];
  j=i-1;
  while(j>=0 && a[j]>temp)
  {
   a[j+1]=a[j];countinsertion++;
   j--;
  }
  a[j+1]=temp;
  i++;
}

}
