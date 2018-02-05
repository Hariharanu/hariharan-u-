a=[]
b=0
n=int(input(" enter the range:"))
for i in range(0,n):
  m=int(input(" enter the list element:"))
  a.append(m)
print("the given array is ")
print(a)
for r in range(0,n):
    b=b+a[r]
print("average value is",b//n)
    
