#     1
#    11
#   1*1
#  1**1
# 11111


n=int(input("Enter the number : "))
i=1
while i<=n:
    j=1
    while j<=n:
        if i+j==n+1 or j==n or i==n:
            print("1",end="")
        elif i+j>n+1 :
            print("*",end="")    
        else:
            print(" ",end="")    
        j+=1
    print()
    i+=1        