m=0
n=input("enter the string: ")
num=len(n)
int(num)
for i in range(0,num):
    if (n[i] =='a' or n[i]== 'e' or n[i]=='i' or n[i]=='o' or n[i]=='u'):
        m="yes"
if m=="yes":
    print("yes")
else:
    print("no")    
