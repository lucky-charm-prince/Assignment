# S = "This is a test"  output : - 4
s=input("Enter the String : ")
s=s.strip()
count=0
for i in range(1,len(s)):
    if s[i-1]==' ' and s[i]!=' ':
        count+=1
if len(s)>0:
    count+=1
print(count)        