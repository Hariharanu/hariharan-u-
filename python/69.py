n=input("enter the number:").split(" ")
map(int,n)
i=(int(n[0])-int(n[1]))
if i%2==0:
    print("even",i)
else:
    print("odd",i)    


