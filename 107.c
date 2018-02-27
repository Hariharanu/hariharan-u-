#include<stdio.h>
void main()
{
	int i,h,k,n;
	char b [50];
	printf("enter the string");
	scanf("%s",&b);
	printf("enter last N numbr");
	scanf("%d",&n);
	for(i=0;b[i]!='\0';i++)
	{
		h++;
	}
	k=h-n-1;
	for(i=k;b[i]!='\0';i++)
	{
		printf("%c",b[i]);
	}
}
