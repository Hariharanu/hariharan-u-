n=input("enter the string:")
n=n.casefold()
m=reversed(n)
if list(n)==list(m):
	print(list(n))
	print("yes")
else:
	print("no")
