#include<stdio.h>
void main()
{
    int a,b,c,m;
    printf("enter tha A,B,C values:");
    scanf("%d%d%d",&a,&b,&c);
    m=(c/2)*(2*a + (c- 1)*b);
    printf("ap is %d",m);
}
