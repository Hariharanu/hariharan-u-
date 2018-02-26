#include<stdio.h>
#include<conio.h>
void main()
{
    int amount,time,rate;
    printf("enter the amount");
    scanf("%d",&amount);
    printf("enter the time");
    scanf("%d",&time);
    printf("enter the rate");
    scanf("%d",&rate);
    int d=(amount*time*rate)/100;
    printf("the floor value is %d",d);
    
}
