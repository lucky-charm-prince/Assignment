# S = "a1b2c3" "123"

s=input("String : ")
s1=""

for i in s:
     if '0'<=i<='9':
          s1+=i
print(s1)