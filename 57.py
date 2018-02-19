#include<stdio.h>
#include<conio.h>
void main()
{
    int a,b;
    printf("enter the tow vlues:");
    scanf("%d%d",&a,&b);
    int c=a;
    a=b;
    b=c;
    printf("%d %d",a,b);
}
