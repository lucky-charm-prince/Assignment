# 57 Merge two strings alternatively.
# S1 = "ABC", S2 = "def" output : - "AdBeCf"

s1=input("String 1 : ")
s2=input("String 2 : ")
l1=len(s1)
l2=len(s2)
s3=""
x=0
while x<l1 and x<l2:
    s3+=s1[x]
    s3+=s2[x]
    x+=1
if l2>l1:
    while x<l2:
        s3+=s2[x]
        x+=1
else:
    while x<l1:
            s3+=s1[x]
            x+=1
print(s3)            

