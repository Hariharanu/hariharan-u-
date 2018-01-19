a=[]
n=int(input("enter the limit :"))
for i in range(0,n):
	m=int(input("enter the element:"))
	a.append(m)
print("The list is",a)
a.sort()
print("Sorted elements are :",a)
t=n//2
if (n%2==0):
    print("This list have no middle elements")
else:                                                                                             
    print(" middle elements is ",a[t])     
