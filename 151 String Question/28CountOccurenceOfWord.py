s=input("Enter the String ")
l1=len(s)
word=input("Word : ")
l2=len(word)
start=0
count=0
for i in range(0,l1):
    if s[i]==' ':
        if l2==i-start and word==s[start:i]:
            count+=1
        start=i+1 
else:
     if l2==l1-start and word==s[start:l1]:
         count+=1
     print("Count : ",count)    