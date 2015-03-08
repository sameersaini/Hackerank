#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {
    int i,j,n,count,a[1000];
    scanf("%d",&n);
    for(i=0;i<n;scanf("%d",&a[i++]));
    
     while(1)
     {  //search for the smallest number
         int small=1001;
	count=0;
         for(i=0;i<n;i++)
         { 
             if(a[i]==0)
             continue;
          for(j=0;j<n;j++)
              {
              if(a[i]<=a[j])
                  {
                  if(a[i]<small)
			         small=a[i];
              }
          }
     }
	if(small==1001) //if array contains only zeros then break
 		break;	
//decrease the size of each array element by smallest number found.	      
	for(i=0;i<n;i++)
       { 
        if(a[i]==0) //if the number inthe array is zore do not decrease it.
	          continue;
           else
          {
              a[i]=a[i]-small;
	        count+=1; //increase the count for decreased numbers
          }
      }
 
printf("%d\n",count);
      
     }
    return 0;
}
