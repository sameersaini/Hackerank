#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
void quicksort(int arr[],int ,int);
int partition(int a[],int,int); 
int main() {
    
    int t;scanf("%d",&t);
    int i,j,n,k,flag;
    while(t--)
        {
         int a[1005],b[1005];
         scanf("%d%d",&n,&k);
         for(i=0;i<n;scanf("%d",&a[i++]));
         for(i=0;i<n;scanf("%d",&b[i++]));
         quicksort(a,0,n-1);
         quicksort(b,0,n-1);
        for(i=0,j=n-1;i<n;i++,j--)
          { 
             flag=0;
             if(a[i]+b[j]>=k)
                {
                 flag=1;
                 continue;
                  }
             else
                 break;
          }
        
               if(flag==0)
                {
                   printf("NO\n");
               }
               else
                 printf("YES\n");
    }
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
