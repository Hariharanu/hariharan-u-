#include<stdio.h>
void main()
{
    int a[10],i,j,m;
    
    for(i=0;i<10;i++)
    {
        scanf("%d",&a[i]);
    }
    for(i=0;i<10;i++)
    {
        for(j=i+1;j<10;j++)
        {
            if (a[i]>a[j])
            {
                m = a[i];
                a[i] =a[j];
                a[j] =m;
 
            }
        }
    }
    
    printf("minimu values ia %d",a[0]);
    
}
