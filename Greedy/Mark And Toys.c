#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
void quicksort(int arr[],int ,int);
int partition(int a[],int,int); 
 

int main() {
    int n, k, i, count;
    scanf("%d%d", &n, &k);
    int *prices = (int *)malloc(sizeof(int)*n);
    for(i=0; i<n; i++) {
        scanf("%d", &prices[i]);
    }
    quicksort(prices,0,n-1);
    int answer = 0;   
    int temp=prices[0];i=1;
    while(k>temp&&i<n)
        {
        if(k>temp)
            {
            k=k-temp;
            temp=prices[i++];
            answer++;
        }
    }
    printf("%d\n", answer);
      
    return 0;
}
void quicksort(int arr[],int low,int high)
    {
    int pivot,i;
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
 if(left>=right)
  return 0;
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
