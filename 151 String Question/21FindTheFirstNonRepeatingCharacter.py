s=input("Enter the String : ")
for i in s:
    count=0
    for j in s :
        if i==j:
            count+=1
        if count>1:
            break
    if count==1:
        print(i)
        break
else:
    print("Not repeating character found ")                
