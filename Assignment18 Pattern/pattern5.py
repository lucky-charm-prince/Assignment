n=int(input("Enter the number : "))
i=1
while i<=n:
    j=1
    while j<=n:
        if i+j>n:
            if(i+j)%2!=0:
                print("0",end="")
            else:
                print("1",end="")
        else:
            print(" ",end="")
        j+=1
    i+=1
    print()