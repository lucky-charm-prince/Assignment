s=input("Enter the string : ")
s1=""
for i in range(len(s)):
    if (65<=ord(s[i])<=90) or (97<=ord(s[i])<=122):
        s1=s[i:]
        break
for i in range(len(s1)-1,-1,-1):
    if (65<=ord(s1[i])<=90) or (97<=ord(s1[i])<=122):
        s1=s1[0:i+1]
        break
print(s1)   