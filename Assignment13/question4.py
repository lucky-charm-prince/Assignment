import math
no=int(input("enter the no="))
val=no
temp=0
sum=0
"""
for i in range(len(str(no))):
    temp=no%10
    math.factorial(temp)
    sum=sum+math.factorial(temp)
    no=no//10
if sum==val:
   print("strong number")
else:
    print("not strong number") """


while no>0:
    temp=no%10
    math.factorial(temp)
    sum=sum+math.factorial(temp)
    no=no//10
if sum==val:
   print("strong number")
else:
    print("not strong number")
  
    