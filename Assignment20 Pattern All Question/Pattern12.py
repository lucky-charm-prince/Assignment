# 12345
#  1234
#   123
#    12
#     1

n=int(input("Enter the number : "))
i=1
while i<=n:
    j=1
    k=1
    while j<=n:
        if j>=i:
            print(k,end="")
            k+=1
        else :
            print(" ",end="")
        j+=1
    print()
    i+=1        

           
        


