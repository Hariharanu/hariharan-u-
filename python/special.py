count=0
a=input("enter the string:")
for i in a:
	if i in ["!","@","$","#","%","^","&","*"]:
		count=count+1
print("special character in the given string are:",count)
