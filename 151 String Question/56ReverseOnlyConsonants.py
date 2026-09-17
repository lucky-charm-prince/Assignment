


s1=input("String : ")
s2=""
s3=""
for i in s1:
    if i not in ['a','e','i','o','u']:
        s2+=i
count=len(s2)-1
for i in s1:
    if i not in ['a','e','i','o','u']:
        s3+=s2[count]
        count-=1
    else:
        s3+=i 
print(s3)           
   