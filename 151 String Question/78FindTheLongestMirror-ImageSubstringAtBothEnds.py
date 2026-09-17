# S = "aabccbaa" output : "aab"

s=input("String : ")
s1=""
for i in range(len(s)):
    if s[0:i]==s[::-1][0:i]:
        s1=s[0:i]
print(s1)        
        