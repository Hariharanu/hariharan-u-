
#include <stdio.h>

int main()
{
     int  i, a[40],n;
   printf(" enter the limit ");
   scanf("%d",&n);
   printf(" enter the numbers");
   for( i=0;i<n;i++)
   {
       scanf("%d",&a[i]);
       
   }int max=0;
   for(i=0;i<n;i++)
   {
   if (a[i]>max)
   {
       max=a[i];
   }}
   printf("%d",max);
    return 0;
}


