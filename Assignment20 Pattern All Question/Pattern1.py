n=int(input("enter the number of rows="))

i=1
while i<=n:
    j=1
    while j<=i:
        if i==j or j==1 or i==n:
            print("*",end="")
        else:
            print(" ",end="")    
        j+=1
    print()    
    i+=1        