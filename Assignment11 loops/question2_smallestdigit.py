no=int(input("enter the no="))
min=10
# for i in range(len(str(no))):
#     d=no%10
#     if min>d:
#         min=d
#     no=no//10
# print("the max no is=",min)

while no>0:
    no=no%10
    if min>no:
        min=no
    no=no//10
print("the no is =",min)