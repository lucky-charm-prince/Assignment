#      1               
#     101            
#    10101         
#   1010101           
#  101010101   
# 10101010101


n=int(input("Enter the number : "))
i=1
while i<=n:
    j=1
    k=1
    while j<=n+i-1:
        if i+j>n:
            if k==1:
                print("1",end="")
                k-=1
            else :
                print("0",end="")    
                k+=1
        else:
            print(" ",end="")
        j+=1
    print("")
    i+=1                