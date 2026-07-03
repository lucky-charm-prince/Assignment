no=int(input("enter the value="))
count=0
# for i in range(1,no+1):
#     if no%i==0:
#         count=count+1
# print("sum=",count)

# now for using the while loop

i=1
temp=no
while no>0:
    if temp%i==0:
        count=count+1
    i=i+1
    no=no/i
print("count=",count)