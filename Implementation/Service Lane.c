#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {
           int arrsize,notest,final,temp,maxsize;
    scanf("%d%d",&arrsize,&notest);
    if((arrsize>=2&&arrsize<=100000)&&(notest>=1&&notest<=1000))
    {
    int a;
        int *lanewidth;
        lanewidth = (int *)malloc(arrsize*sizeof(int));
    for(a=0;a<arrsize;a++)
       {
            scanf("%d",&temp);
            if(temp>=1&&temp<=3)
               lanewidth[a]=temp;
        }
            
        int testcount;
        for(testcount=1;testcount<=notest;testcount++)
            {
              final=1;
            int i,j,count,copyi;
            scanf("%d%d",&i,&j);
            if(i>=0&&i<j&&j<arrsize)
                {
                for(maxsize=1;maxsize<=3;maxsize++)
                { copyi=i;
                  while(copyi<=j)
                  {  
                   if(maxsize<=lanewidth[copyi])
                        {
                        
                        if(copyi==j)
                            {
                            final=maxsize;
                            
                        }
                       copyi++;
                }
                    else
                        {
                         break;
                        }
                    }
                      
                }
            }
             printf("%d\n",final);
            }
           
            }
    return 0;
        }

  
