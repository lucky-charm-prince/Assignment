n=int(input("enter the no="))
# update=len(str(n))-1
# temp=0
# for i in range(len(str(n))):
#     temp=n%10
    
#     if i==update:
#         print("the first digit=",n)
#     n=n//10
   
temp=0
while n>0:
    temp=n%10
    n=n//10
print("the first digit=",temp)