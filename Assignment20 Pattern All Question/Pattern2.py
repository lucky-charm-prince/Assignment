n=int(input("enter the number of rows="))

i=1
while i<=n:
    j=1
    while j<=i:
        if i==j or j==1 or i==n:
            print(j,end="")
        else:
            print(" ",end="")    
        j+=1
    print()    
    i+=1        

# 1
# 12
# 1 3
# 1  4
# 12345
