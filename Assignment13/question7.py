no=int(input("enter the no"))
temp=0
sum=0
"""
for i in range(len(str(no))):
    temp=no%10
    if temp==0:
        sum=sum+1
    no=no//10
if sum>=1:
   print("duck number")
else:
   print("no duck number") """

"""using while loop"""

while no>0:
     temp=no%10
     if temp==0:
        sum=sum+1
     no=no//10
if sum>=1:
   print("duck number")
else:
   print("no duck number")
    