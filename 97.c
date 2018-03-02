#include<stdio.h>
void main()
{
    int i,m;
    scanf("%d",&i);
    while(i!=0)
    {
        m=i%10;
        i=i/10;
        printf("%d",m);
        
    }
}
