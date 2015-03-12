#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
int maxsum(int a[],int);
int maxnoncsum(int a[],int);
int main() {
    int a[100001], maxnoncontsum=0;
    int t,n;scanf("%d",&t);
    while(t--)
        {
         scanf("%d",&n);
         int i;
           for(i=1;i<=n;scanf("%d",&a[i++]));
         int maxcontsum=maxsum(a,n);
         int maxnoncontsum = maxnoncsum(a,n);
        printf("%d %d\n",maxcontsum,maxnoncontsum);
    }
    return 0;
}


int maxsum(int a[],int n)
    {
     int val;int flag=0;int min=-10001;
     int currentsum=0;
     int currentindex=0;
     int bestsum=0;
     int i;
     for(i=1;i<=n;i++)
         {
         val =  currentsum + a[i];
         if (val > 0)
             {
	      flag=1;
              if(currentsum==0)
                  {
                   currentindex=i;
              }
              currentsum=val;
              
              }
          else
          {
           currentsum=0;
          }
         if(currentsum>bestsum)
          {
             bestsum=currentsum;
         }   
         }
for(i=1;i<=n;i++)
   {
    if(a[i]<0&&flag==0)
     {
      if(a[i]>min)
	{
  	 min=a[i];
	 }
     } 
   }
if(flag==1)
{
 return bestsum;
}
else
{
 return min;
}
    return bestsum;
}
int maxnoncsum(int a[],int n)
{
 int i,min=-10001;int flag=0;int maxnoncontsum=0;
 for(i=1;i<=n;i++)
   {
    if(a[i]>0)
    { 
      flag=1;
      maxnoncontsum += a[i];
    }
   }
   for(i=1;i<=n;i++)
   {
    if(a[i]<0&&flag==0)
     {
      if(a[i]>min)
	{
  	 min=a[i];
	 }
     } 
   }
if(flag==1)
{
 return maxnoncontsum;
}
else
{
 return min;
}
}