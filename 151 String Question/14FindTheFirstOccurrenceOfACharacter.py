s=input("Enter the String : ")
c=input("Enter the char : ")
count=0
for i in s:
    if i==c:
        print(count)
        break
    count+=1
else:
    print("NOtFound")    