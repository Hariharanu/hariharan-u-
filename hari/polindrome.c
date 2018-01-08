#include <stdio.h>
void  main()
{
    int a,b,c,revers_b;
    printf ("enter the number:\n");
    scanf("%d",&a);
 while(a>10)  
 {  
     b=a%10;
    revers_b=revers_b*10+b;
    a/=10;
     
 }
    
    if(a==revers_b)
    {
        printf("polidrome");}
       
        else
       { 
        printf("not polindrome");
       }
}


