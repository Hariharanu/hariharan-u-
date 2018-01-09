#odd or even number between 2 intervels 
def m():
	n=int(input("enter the  first number:"))
	k=int(input("enter the second number :"))
	a=[]
	for i in range(n,k):
		if i%2==0:
			print("even number and even number is ",i)
            
		else:
			print("odd number and odd number is",i)
			print("prime number :",i)
	m()     
		
m()
