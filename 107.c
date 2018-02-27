#include<stdio.h>
void main()
{
	int i,j,k;
	printf("enter the 3 numbers");
	scanf("%d%d%d",&i,&j,&k);
	int m=(i*j)%k;
	printf("%d",m);
}
