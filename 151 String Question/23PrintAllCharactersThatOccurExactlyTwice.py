s=input("Enter the String : ")
x=""
for i in s:
    if i not in x:
        x+=i
        count=0
        for j in s:
            if i==j:
                count+=1
        if count==2:
            print(i)        