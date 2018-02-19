m=int(input("enter the number:"))
n=0
for num in range(2,m):
    if num > 1:
        for i in range(2,num):
            if (num % i) == 0:
                n=9
    else:
        print(num,"neither prime nor compsite")
if n==9:

    print("yes",m)
else:
    print("no",m)
