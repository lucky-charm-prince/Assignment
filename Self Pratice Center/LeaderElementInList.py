n=list(map(int,input("Enter the list : ").split(",")))
k=len(n)-1
for i in range(len(n)-1,-1,-1):
    if i==(len(n)-1):
        print(n[i],end=" ")
    else:
        if n[i]>k:
            print(n[i],end=" ")
            k=n[i]