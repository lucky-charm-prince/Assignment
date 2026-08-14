import sys
s=input("Enter the string : ")
n=sys.maxsize
for i in s:
    count=0
    for j in s:
        if j==i:
            count+=1
    if n>count:
        n=count
print(n)                

x=""

for i in range(len(s)):
    count=0
    for j in range(0,len(s)):
        if s[j]==s[i]:
            count+=1
    if n==count:
        if s[i] not in x:
            x+=s[i]
print(x)             