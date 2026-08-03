#     1
#    10 
#   101
#  1010
# 10101


n=int(input("Enter the number : "))
i=1
while i<=n:
    j=1
    k=1
    while j<=n:
        if i+j>=n+1 or j==n or i==n:
           
            if k%2==1:
                print("1",end="")
                k=0
            else:
                print("0",end="")    
                k+=1
        
        else:
            print(" ",end="")    
        j+=1
    print()
    i+=1        