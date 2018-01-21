a=[]
n=int(input(" enter the range:"))
for i in range(0,n+1):
  m=int(input(" enter the list element:"))
  a.append(m)
print("list is ",a)
for r in a:
  print("index of",r,"is",a.index(r))
