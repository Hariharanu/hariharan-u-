#include<stdio.h>
void main()
{
    int a[100],i,j,m,n,b[100],count=0;
    printf("enter the limit ");
    scanf("%d",&n);
    for(i=0;i<n;i++)
    {
        scanf("%d",&a[i]);
    }
    for(i=0;i<n;i++)
    {
        b[i]=a[i];
    }
    for(i=0;i<n;i++)
    {
        for(j=i+1;j<n;j++)
        {
            if (a[i]>a[j])
            {
                m = a[i];
                a[i] =a[j];
                a[j] =m;
 
            }
        }
    }
     for(i=0;i<n;i++)
     {
         if(a[i]!=b[i])
         {
            count++; 
            printf("%d",b[i]);
         }
     }
     printf("\n%d",count);
    
   
}
