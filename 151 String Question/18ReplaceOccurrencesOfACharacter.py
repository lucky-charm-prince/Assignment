s=input("Enter the String : ")
old=input("remove char")
rep=input("New char : ")
s1=""
for i in s:
    if i==old:
        s1+=rep
    else:
        s1+=i
print(s1)            