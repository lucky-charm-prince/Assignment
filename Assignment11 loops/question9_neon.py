no=int(input("enter the no="))
temp=no
count=0
# for i in range(len(str(no))):
#     d=no**2
# for i in range(len(str(d))):
#     sum=d%10
#     count=count+sum
#     d=d//10
# if no==count:
#     print("found no  ")
# else:
#     print("not found")
square=no**2
while square!=0:
    d=square%10
    count=count+d
    square=square//10
    
if temp==count:
    print("no is found ")
else:
    print("no is not found")
