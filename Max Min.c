#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

#define MAX 100000
#define MAX_VAL 1000000001


int candies[MAX];

void quicksort(int x[],int first,int last);
int partition(int a[],int low,int high);
int main() {
    
    int N,K;
    int i,j,temp;
    int ans,min;
    
    scanf("%d %d",&N,&K);
    for(i = 0;i < N;scanf("%d",&candies[i++]));
     min=MAX_VAL;
    quicksort(candies,0,N-1);

    for(i=0;i+K-1<N;i++)
        {
         ans=candies[i+K-1]-candies[i];
  
         if(ans<min)
            min=ans;
          }
   printf("%d",min);
    return 0;
}
 void quicksort(int arr[],int low,int high)
    {
    int pivot;
	if(high>low)
	{
	pivot=partition(arr,low,high);
	quicksort(arr,low,pivot-1);
	quicksort(arr,pivot+1,high);
   
    }    
}
int partition(int a[],int low,int high)
{
 int pivot_value=a[low];int temp;int left,right,i;
 left=low;
 right=high;
 while(left<right)
 {
  while(a[left]<=pivot_value&&left<right)
    left++;
  while(a[right]>pivot_value)
    right--;
  if(left<right)
  {
   temp=a[left];
   a[left]=a[right];
   a[right]=temp;
   }

}
a[low]=a[right];
a[right]=pivot_value;
return right;
} 