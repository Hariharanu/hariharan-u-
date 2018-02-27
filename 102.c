#include<stdio.h>
int rec(int);
void main()
{
  int a,b;
  printf("enter the number:");
  scanf("%d",&a);
  rec(a);
  	
}
int rec(int a){
	if (a%2==0)
	{
		a=rec(a/2);
	}
	else
	{
		printf("%d",a);
	}
	return 0;}

