# polindrome
def me(i):
	if i%2==0:
		print("not prime number")
	else:
		print("prime number") 
def m():
	mystr=input("enter the string :")
	mystr=mystr.casefold()
	reverstr=reversed(mystr)
	if list(mystr)==list(reverstr):
		print("polindrome")
		print(list(mystr))
		me(mystr)
	else:
		print ("not polindrome")
		print (list(reverstr))
		me(mystr)
m()


