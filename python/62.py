n=input("enter the number:")
c=0
for i in range(0,len(n)):
	if int(n[i])==0  or int(n[i])==1:
	    c="yes"
	else:
		c="no"
if c=="yes":
	print("yes")
else:
	print("no")


        
