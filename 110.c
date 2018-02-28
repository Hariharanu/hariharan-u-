#include<stdio.h>
void main()
{
    int a,i,j=0;
    
    printf("enter the number:");
    scanf("%d",&a);
    for(i=1;i<=a;i++)
    {
        j=j+i;
    }
    printf("sum of tha number is %d",j);
}
