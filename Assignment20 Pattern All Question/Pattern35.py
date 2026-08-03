# *         *
#  *      *
#    *  *
#     *
#    *  *
#  *      *
# *         *


n=int(input("Enter the number : "))

i=1
while i<=n*2-1:
    j=1
    while j<=n*2-1:
        if i==j or i+j==n*2:
            print("*",end=" ")
        else:
            print(" ",end=" ")    
        j+=1
    print("")        
    i+=1