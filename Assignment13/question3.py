"""
a,b=map(int,(input("enter the no=")).split())
print(15%10)
for i in range(a,b+1):
    if i%10==5:
       print(i,end=" ")
    else:
       continue """

a,b=map(int,(input("enter the no=")).split())

while a<b:
    
    if a%10==5:
       print(a,end=" " )
    a=a+1
    
    