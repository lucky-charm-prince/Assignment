# S = "hello" output:- "he$lo"


s=input("String : ")
s1=""
for i in range(len(s)):
    for j in range(i+1,len(s)):
        if s[i]==s[j]:
            s1+="$"
            break
    else    :
        s1+=s[i]+""
print(s1)        