no=int(input("enter the no="))
temp=1
power=1
# for i in range(len(str(no))):
#         temp=no%10
#         sum=no//10
#         no=no//10
#         power=sum**temp
# print("power=",power)

while no>0:
    temp=no%10
    sum=no//10
    power=sum**temp
print("power=",power)
    