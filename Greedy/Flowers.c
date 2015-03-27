/* Sample program illustrating input/output methods */
#include<stdio.h>
int main(){

//Helpers for input/output
   int i,j,t, N, K,temp;
    long int result;
   int C[102];
   result=0;
   scanf("%d %d", &N, &K);
    t=K;
   for(i=0; i<N; i++){
      scanf("%d", &C[i]);
   }
   for(i=0;i<N-1;i++)
        {
        for(j=0;j<N-i-1;j++)
            {
            if(C[j]>C[j+1])
                {
                temp=C[j];
                C[j]=C[j+1];
                C[j+1]=temp;
            }
        }        
    }
    j=0;
    for(i=N-1;i>=0;i--)
       {
        result=result+(j+1)*C[i];
        t--;
        if(t==0)
            {
            t=K;
            j++;
        }
        
    }
   
   printf("%ld\n", result);

}
