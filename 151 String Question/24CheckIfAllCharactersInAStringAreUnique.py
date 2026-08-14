s=input("Enter the String : ").lower()
for i in s:
    count=0
    for j in s :
        if i==j:
            count+=1
    if count>1:
        print("False")
        break       
else:
    print("True")     