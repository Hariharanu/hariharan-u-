n=int(input("enter the number:"))
m,k=input("enter the starting and ending point:").split(" ")
j=0
for i in range(int(m),int(k)):
    if n==i:
        j+=1
if j==0:
    print("on")
else:
    print("yes")
