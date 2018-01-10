
n=int(input("enter the starting point:"))
m=int(input("enter the ending point"))
for num in range(n,m):
    if num > 1:
        for i in range(2,num):
            if (num % i) == 0:
                print(num,"is not a prime number")
                print(i,"times",num//i,"is",num)
                break
            else:
                print(num,"is a prime number")
    else:
        print(num,"is not a prime number")
