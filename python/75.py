n=list(input("enter the string:"))
m=len(n)
t=m//2
if int(m)%2==0:
	print("this string has no middel element")
else:
	n[t]="*"
print("".join(n))
