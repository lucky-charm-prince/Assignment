# S = "a1b2c3" output :- "abc"


s=input("String : ")
s1=""
for i in s:
    if '0'<=i<='9':
        s1=s1
    else:
        s1+=i
print(s1)            