no=int(input("enter the no="))
temp=0
org=no
sum=0
"""
for i in range(len(str(no))):
    temp=no%10
    sum=sum+temp
    no=no//10
if org%sum==0:
   print("harshad number")
else:
   print("not harshad number")"""


while no>0:
    temp=no%10
    sum=sum+temp
    no=no//10
if org%sum==0:
   print("harshad number")
else:
   print("not harshad number")
