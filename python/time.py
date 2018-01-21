n=int(input("enter the mins:"))
if n>60:
  a=n//60
  b=n-(a*60)
  print("Time is",a,":",b)
else:
  print("time is ","00:",n)
  
