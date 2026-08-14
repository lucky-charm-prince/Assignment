s=input("Enter the String : ")
max=0
ch=''
for i in range(len(s)) :
    count=1
    for j in range(i+1,len(s)):
        if s[i]==s[j]:
            count+=1
    if count>max:
        max=count     
        ch=s[i]
print(ch,max)           