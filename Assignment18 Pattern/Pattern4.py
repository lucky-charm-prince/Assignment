n=int(input("Enter the number :  "))
i=1
while i<=n:
    j=1
    k=n+1
    while j<=n+1:
        if j<=i-1:
            print(" ",end="")
        else:
            print(k,end="")
            k-=1
        j+=1
    print()    
    i+=1    