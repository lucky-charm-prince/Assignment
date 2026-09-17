s=input("String : ")
s1=""

for i in s:
    if 'a'<=i<='z' or  'A'<=i<='Z' or '0'<=i<='9':
        s1+=i
print(s1)        
        