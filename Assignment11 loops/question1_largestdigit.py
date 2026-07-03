no=int(input("enter the no="))
# max=0
# for i in range(len(str(no))):
#     d=no%10
#     if max<d:
#         max=d
#     no=no//10
# print("the max no is=",max)

# using the while loop
max=0
while no>0:
    no=no%10
    if max<no:
        max=no
    no=no//10 
print("the gargest digit is =",max)