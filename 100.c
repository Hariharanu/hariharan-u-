#include<stdio.h>
void main()
{
    int i,m,count=0,sum=1;
    scanf("%d",&i);
    while(i!=0)
    {
        m=i%10;
        i=i/10;
        count++;
        
    }
    for(i=1;i<=count;i++)
    {
        sum=sum*i;
    }
    printf("%d",sum);
}
