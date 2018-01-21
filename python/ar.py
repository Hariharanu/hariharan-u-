def is_arithmetic(l):
    delta = l[1] - l[0]
    for index in range(len(l) - 1):
        if not (l[index + 1] - l[index] == delta):
             print(" This sequence is not arithmatic progression")
             break
    print("this sequence is arithmetic sequence")
    tn=(l[0]+(len(l)-1))*delta
    print(" tn value is tn=",tn)
    break       

a=[]
n=int(input(" enter the range:"))
for i in range(0,n+1):
  m=int(input(" enter the sequence:"))
  a.append(m)
          
is_arithmetic(a)
