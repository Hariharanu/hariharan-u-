n=int(input("enter the limit:"))
n1=0
n2=1
count=0
print("fiboncci series is")
while count<n:
    print(n1,end=' , ')
    nt = n1 + n2
    n1 = n2
    n2 = nt
    count += 1
