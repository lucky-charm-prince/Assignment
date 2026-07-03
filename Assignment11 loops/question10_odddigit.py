no=int(input("enter the no="))
count=0
# for i in range(len(str(no))):
#     tem=no%10
#     if tem%2!=0:
#         count=count+1
#     no=no//10
# print("count=",count)
while no>0:
    temp=no%10
    if temp%2!=0:
        count=count+1
    no=no//10
print("count=",count)