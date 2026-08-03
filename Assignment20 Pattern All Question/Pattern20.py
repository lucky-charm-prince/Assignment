# 123456789
#  1234567
#   12345
#    123
#     1


n=int(input("Enter the number : "))

i=1
while i<=n:
    j=1

    k=1
    while j<=n*2-1:
        if j>=i and i+j<=n*2:
            print(k,end="")
            k+=1
        else:
            print(" ",end="")    
        j+=1
    print("")
    i+=1        
