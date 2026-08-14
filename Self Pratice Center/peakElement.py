n=list(map(int,input("Enter the list : ").split(",")))
k=0
if len(n)==1:
    print(n[0])
elif len(n)==2:
    if n[0]>n[1]:
        print(n[0])
    else:
        print(n[1])
elif len(n)>2:
    if n[0]>n[1]:
        k+=1
        print(n[0])
    for i in range(2,len(n)-1):
        if n[i+1]<n[i]>n[i-1]:
            print(n[i])
            k+=1
            break
    if (n[len(n)-1]>n[len(n)-2]) and (k==0):
        print(n[len(n)-1])
 