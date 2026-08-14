s=input("Enter the String ")
x=1
for i in range(len(s)-1,-1,-1):
    count=0
    for j in range(len(s)-1,-1,-1):
        if s[i]==s[j]:
            count+=1
            if count==2:
                print(s[i])
                x=0
                break
    if x==0:
        break
    