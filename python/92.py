n=int(input("enter the limit"))
j=0
k=input("enter the number ")
if len(k)<=n:
    for i in range(0,len(k)):
        j=j+int(k[i])
        print(j)
    
else:
    print("enter only",n,"numers")    

    
