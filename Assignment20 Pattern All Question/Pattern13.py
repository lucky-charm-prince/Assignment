# ABCDE
#  A__D
#   A_C
#    AB
#     A


n=int(input("Enter the number : "))
i=1
while i<=n:
    j=1
    k=65
    while j<=n:
        if j==i or j==n or i==1:
            print(chr(k) ,end="")
            k+=1
        elif  j-i>0:
            print("_",end="")
            k+=1
        else:

            print(" ",end="")    
        j+=1
    print()
    i+=1        


# 11 12 13 14 15
# 21 22 23 24 25 
# 31 32 33 34 35
# 41 42 43 44 45
# 51 52 53 54 55            
        



