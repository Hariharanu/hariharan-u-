summ=0   
num=int(input("enter the number :"))
k=int(input("enter the number:"))
for i in range(num,k):
	while i>10:
		digit=i%10
		summ=summ+digit**3
		i//10
	if i==digit:
		print("amstrong number")
	else:
		print("not amstrong number")
		
