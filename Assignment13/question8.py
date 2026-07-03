no=int(input("enter the no="))
org=no
rev=0
temp=0
count=0
"""
for i in range(len(str(no))):
    temp=no%10
    rev=rev*10+temp
    no=no//10
diff= rev-org
for i in range(len(str(diff))):
    count=count+1
if diff==0:
   print("perfect match ")
elif diff%9==0:
    print("verified")
else:
    print("rejected") """

while no>0:
   temp=no%10
   rev=rev*10+temp
   no=no//10

diff= rev-org
for i in range(len(str(diff))):
    count=count+1
if diff==0:
   print("perfect match ")
elif diff%9==0:
    print("verified")
else:
    print("rejected")

   