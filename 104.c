#include<stdio.h>
void main()
{
	int n,k,i,sum=1;
	printf("enter the N and k value");
	scanf("%d%d",&n,&k);
	for( i=1;i<=k;i++)
	{
	sum=sum*n;
	}
printf("%d",sum);
}
