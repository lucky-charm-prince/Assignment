# S = "abracadabra"   output :"abra"

s=input("String")
s1=""

for i in range(len(s)):
    if (s[0:i]==s[len(s)-i:len(s)]) and (len(s[0:i])>len(s1)):
        
        s1=s[0:i]
print(s1)        
    