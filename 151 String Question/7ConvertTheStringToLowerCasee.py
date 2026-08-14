s=input("Enter the String : ")
s1=""
for i in s:
    if 65<=ord(i)<=90:
        s1+=chr(ord(i)+32)
    else:
        s1+=i
print(s1)            