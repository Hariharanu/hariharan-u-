n=list(input("enter sting :"))
m=[]
b=[]
for i in range(0,len(n)):
    if i%2==0:
        m.append(n[i])
    else:
        b.append(n[i])
print("".join(m),end=' ')
print("".join(b),end='')
        
        
