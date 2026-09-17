# S = "babad" output : "bab" (or "aba")


s=input("String")
s1=""
for i in range(len(s)):
    for j in range(i,len(s)):
        str=s[i:j]
        if str==str[::-1] and len(str)>len(s1):
            s1=str
print(s1)            