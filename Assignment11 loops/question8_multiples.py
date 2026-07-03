a,b=map(int,(input("enter the two no=")).split(" "))
count=0
# for i in range(a,b+1):
#     if i%5==0:
#         count=count+1
# print("the count=",count)
while a<=b:
    if a%5==0:
        count=count+1
    a=a+1
print("count=",count)
