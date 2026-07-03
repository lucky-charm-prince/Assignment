n=int(input("Enter the number : "))
for i in range(1,n+1):
    #x=65
    x=97
    for j in range(1,i+1):
        print(chr(x),end="")
        x+=1
    print()
